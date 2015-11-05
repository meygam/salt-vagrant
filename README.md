# salt-vagrant

To test the salt-api pagerduty integration

* bring up the salt master (master) & two minions (minion1, minion2) `vagrant up`
* run the highstate on master to setup the salt-api `salt-call state.highstate`
* test if all the minions are connected to master `salt '*' test.ping`
* create dummy log files in minions using the helper script `/vagrant/helper_scripts/create_logs.sh`
* share the vagrant box to make it available to the world `vagrant share master`, and get the url.
* hook up the salt-master url `http://<<salt-master>>/hook/meygam/pagerduty/salt-api-test/incident` to pagerduty service
* create a dummy incident with the below descriptions
  ```
  server minion1.meygam.com is reporting High Volume Usage
  
  server minion2.meygam.com is reporting High Volume Usage
  ```
* the incident would trigger the reactor `cleanup_logs`, which in turn starts the orchestartion `orch.meygam.util.cleanup_logs`, to delete the logs in the respective minion and resolve the pagerduty.
