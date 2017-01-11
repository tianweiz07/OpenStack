# OpenStack
OpenStack for monitoring VM's health

include horizon, novaclient and nova

Modify horizon:
  horizon/openstack_dashboard/dashboards/project/instances/tables.py
  horizon/openstack_dashboard/dashboards/project/instances/workflows/update_instance.py

  horizon/openstack_dashboard/api/nova.py

Modify novaclient:
  novaclient/v2/servers.py

Modify nova:
  nova/nova/api/openstack/compute/servers.py
  nova/nova/db/sqlalchemy/migrate_repo/versions/216_havana.py
  nova/nova/api/openstack/compute/attest_service.py

  nova/nova/objects/request_spec.py
  nova/nova/db/sqlalchemy/migrate_repo/versions/216_havana.py
  nova/nova/compute/api.py
  nova/nova/scheduler/filters/availability_zone.py
  nova/nova/scheduler/host_manager.py
  nova/nova/scheduler/utils.py
