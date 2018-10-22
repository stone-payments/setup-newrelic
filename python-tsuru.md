# Python tsuru
Running a python application with New Relic on Tsuru.

### Environment variables:
| Var name  | Value |
| ------------- | ------------- |
| NEW_RELIC_CONFIG_FILE | /tmp/newrelic.ini |
| NEWRELIC_KEY | New Relic application key |
| NEWRELIC_APP_NAME | Application name on the New Relic dashboard |

### Tsuru.yaml:
You should run the **setup_newrelic.py** script to generate the config file by adding an hook to the Tsuru.yaml file.
```
hooks:
    build:
        - python setup_newrelic.py
```

### Requirements.txt:
Add newrelic as a dependency.
```
newrelic
```

### Procfile:
Run the application from newrelic-admin
```
web:newrelic-admin run-program python main.py
```

### Expected behavior:
The application should log something like this:
```
2018-10-22 INFO - New Relic Python Agent (4.4.1.104)
2018-10-22 INFO - Successfully registered New Relic Python agent where app_name='***', pid=1, redirect_host='***.newrelic.com' and agent_run_id='***', in 1.77 seconds.
2018-10-22 INFO - Reporting to: https://rpm.newrelic.com/accounts/***/applications/***
```
