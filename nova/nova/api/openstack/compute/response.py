#!/usr/bin/python
#
# This file is to take some countermeasures when something is wrong
#
#
#
#

import os
import time
import sys
import libvirt
from novaclient import client

def vcpu_pin(uuid, host_addr, user_name):
    """
        This function uses Libvirt API to vcpu pin
    """
    conn=libvirt.open("qemu+ssh://"+user_name+"@"+host_addr+"/system")
    dom0 = conn.lookupByUUIDString(uuid)

    NUM_CORE = len(dom0.vcpus()[1][0])

    for vcpu in range(len(dom0.vcpus()[0])):
        vcpu_id = dom0.vcpus()[0][vcpu][0]
        vcpu_location = list(dom0.vcpus()[1][vcpu])
        for i in range(len(vcpu_location)):
            if vcpu_location[i] == True:
                vcpu_location[i] = False
                vcpu_location[(i+1)%NUM_CORE] = True
                break

        dom0.pinVcpu(vcpu_id, tuple(vcpu_location))

def vm_terminate(uuid):
    creds = {}
    creds['username'] = "admin"
    creds['api_key'] = os.environ['OS_PASSWORD']
    creds['auth_url'] = os.environ['OS_AUTH_URL']
    creds['project_id'] = os.environ['OS_TENANT_NAME']
    nova = client.Client("2", **creds)

    instance = nova.servers.get(uuid)

    try:
        instance.delete()
    except Exception:
        sys.exc_clear()

def vm_suspend(uuid):
    creds = {}
    creds['username'] = "admin"
    creds['api_key'] = os.environ['OS_PASSWORD']
    creds['auth_url'] = os.environ['OS_AUTH_URL']
    creds['project_id'] = os.environ['OS_TENANT_NAME']
    nova = client.Client("2", **creds)

    instance = nova.servers.get(uuid)

    try:
        instance.suspend()
    except Exception:
        sys.exc_clear()

def vm_resume(uuid):
    creds = {}
    creds['username'] = "admin"
    creds['api_key'] = os.environ['OS_PASSWORD']
    creds['auth_url'] = os.environ['OS_AUTH_URL']
    creds['project_id'] = os.environ['OS_TENANT_NAME']
    nova = client.Client("2", **creds)

    instance = nova.servers.get(uuid)

    try:
        instance.resume()
    except Exception:
        sys.exc_clear()

def vm_migrate(uuid, dest_addr)
    creds = {}
    creds['username'] = "admin"
    creds['api_key'] = os.environ['OS_PASSWORD']
    creds['auth_url'] = os.environ['OS_AUTH_URL']
    creds['project_id'] = os.environ['OS_TENANT_NAME']
    nova = client.Client("2", **creds)

    instance = nova.servers.get(uuid)

    try:
        instance.live_migrate(dest_addr, True, False)
    except Exception:
        sys.exc_clear()

def vm_migrate(uuid, sour_addr, sour_user_name, dest_addr, dest_user_name):
    """
        This function uses Libvirt API to do VM migration
    """
    sour_conn=libvirt.open("qemu+ssh://"+sour_user_name+"@"+sour_addr+"/system")
    dest_conn=libvirt.open("qemu+ssh://"+dest_user_name+"@"+dest_addr+"/system")

    dom0 = sour_conn.lookupByUUIDString(uuid)

    dom0.migrate(dest_conn, 1, None, None, 0)

