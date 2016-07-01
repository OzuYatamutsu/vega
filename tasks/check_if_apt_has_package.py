## Checks if my apartment has a package ready for pickup.
from tasks.browser_task import BrowserTask

HUMAN_STR = "You %s a package available for pickup."

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
    result = "package" in get_text_from_class(browser, 'alert-list').lower()
    text = "have" if result else "do not have"
    return (text, "green" if not result else "red")  
    print(text)
    
task = BrowserTask(name = task, run_func = run, humanized_template = HUMAN_STR)
task.run()
task.commit_result()
