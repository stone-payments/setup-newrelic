# Setup newrelic
Generate the New Relic config file from environment variables.

This script will generate the config file on **/tmp/newrelic.ini** and set the log file path to **/tmp/newrelic-python-agent.log**

### Running:

##### 1) Set environment vars:
| Var name  | Description |
| ------------- | ------------- |
| NEWRELIC_KEY | New Relic application key |
| NEWRELIC_APP_NAME | Application name on the New Relic dashboard |


##### 2) Command:
```
python setup_newrelic.py
```

### Requirements:
- python (Tested with 2.7x and 3.6x)



### Warning:
- Remember to set the config file path as an environment variable **before** starting the newrelic agent.

| Var name  | Value |
| ------------- | ------------- |
| NEW_RELIC_CONFIG_FILE | /tmp/newrelic.ini |
