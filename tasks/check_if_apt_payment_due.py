## Checks if my apartment payment is due.
from tasks.browser_task import BrowserTask

HUMAN_STR = "Your rent is %s."

def run(browser):
    url = "https://milestonecorporate.residentportal.com/resident_portal/"
    print("Navigating.")
    browser.get(url)
    
    email, password = get_cred(url)
    print("Setting email.")
    set_value(browser, '#email', email)
    print("Setting password.")
    set_value(browser, '#password', password)

    print("Submitting form.")
    browser.execute_script("this.handleLogin()")

    print("Navigating.")
    browser.get(url)
    
    print("Getting value.")
    text = get_text_from_class(browser, 'pay-amount')
    is_green = "green" in browser.find_element_by_class_name('pay-amount').get_attribute('class')
    text = ("-" + text) if (is_green and float(text.replace('$', '').replace(',', '')) > 0) else text
    return (text, "green" if is_green else "red")
    #return (text, "green" if float(text.replace("$", "").replace(",", "")) <= 0.0 else "red")  
    print("Amount due: " + text)
    
task = BrowserTask(name = task, run_func = run, humanized_template = HUMAN_STR)
task.run()
task.commit_result()
