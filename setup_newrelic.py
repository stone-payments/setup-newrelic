import os

config_file = '''
[newrelic]
license_key = {key}
app_name = {name}
monitor_mode = true
log_level = info
high_security = false
transaction_tracer.enabled = true
transaction_tracer.transaction_threshold = apdex_f
transaction_tracer.record_sql = obfuscated
transaction_tracer.stack_trace_threshold = 0.5
transaction_tracer.explain_enabled = true
transaction_tracer.explain_threshold = 0.5
transaction_tracer.function_trace =
error_collector.enabled = true
error_collector.ignore_errors =
browser_monitoring.auto_instrument = true
thread_profiler.enabled = true
distributed_tracing.enabled = false
log_file = /tmp/newrelic-python-agent.log

[newrelic:development]
monitor_mode = false

[newrelic:test]
monitor_mode = false

[newrelic:staging]
app_name = {name} (Staging)
monitor_mode = true

[newrelic:production]
monitor_mode = true
'''

print('''
         ---------------------------------------------
         -------- Generating NewRelic config...-------
         ---------------------------------------------''')

with open('/tmp/newrelic.ini', 'w') as config:
    config.write(config_file.format(key=os.environ.get("NEWRELIC_KEY"), name=os.environ.get("NEWRELIC_APP_NAME")))

print('''
         ---------------------------------------------
         ------------ NewRelic config ok -------------
         ---------------------------------------------''')
