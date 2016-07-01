## Checks if my electricity bill is due.
from tasks.browser_task import BrowserTask

HUMAN_STR = "Your electricity bill is %s."

def run(browser):
    url = "https://coautilities.com/wps/myportal/occ/login"
    print("Navigating.")
    browser.get(url)
    
    email, password = get_cred(url)
    print("Setting email.")
    set_value(browser, "[name='username']", email)
    print("Setting password.")
    set_value(browser, "[name='password']", password)
    
    print("Submitting form.")
    browser.find_element_by_id('LoginForm').submit()
    
    print("Waiting...")
    wait_for_class(browser, 'container12')
    
    print("Getting value.")
    inject_jquery(browser)
    browser.execute_script("$('.occ_value.occ_bodyBold').attr('id', 'tar')")
    text = get_text_from_id(browser, 'tar')
    return (text, "green" if float(text.replace("$", "").replace(",", "")) <= 0.0 else "red")  
    print("Amount due: " + text)
    
task = BrowserTask(name = task, run_func = run, humanized_template = HUMAN_STR)
task.run()
task.commit_result()
