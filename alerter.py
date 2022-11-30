alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    if celcius <= 200:
        return 200
    else:
        return celcius
        
def farenhiet_to_celcius(farenheit):
    return (farenheit - 32) * 5 / 9

def alert_in_celcius(farenheit):
    returnCode = network_alert_stub(farenhiet_to_celcius(farenheit))
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 0
        assert returnCode == 500, f'Temperature observed is {returnCode} Celcius which is beyond Threshold Temperature 200 Celcius'

alert_in_celcius(400.5)
alert_in_celcius(303.6)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
