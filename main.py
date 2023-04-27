import log_in, log_out
import time, sched

def hhhh(schedular):
    schedular.enter(120, 1, hhhh, (schedular,))
    log_out.logOut_requests()
    print('Logged out')
    log_in.logIn_requests()
    print('Logged in')
my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(120, 1, hhhh, (my_scheduler,))
my_scheduler.run()

