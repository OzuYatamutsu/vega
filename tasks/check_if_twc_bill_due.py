## Checks if my electricity bill is due.
from tasks.browser_task import BrowserTask

HUMAN_STR = "Your TWC bill is %s."

def run(browser):
    url = "https://myservices.timewarnercable.com"
    print("Navigating.")
    browser.get(url)
    
    username, password = get_cred(url)
    print("Setting username.")
    set_value(browser, "[name='username']", username)
    print("Setting password.")
    set_value(browser, "[name='password']", password)
    
    print("Clicking button.")
    browser.find_element_by_class_name('sign-in-btn').click()
    
    print("Waiting...")
    wait_for_class(browser, 'balance-summary')
    
    print("Getting value.")
    inject_jquery(browser)
    browser.execute_script("$('.total > .amount').attr('id', 'tar')")
    text = get_text_from_id(browser, 'tar')
    return (text, "green" if float(text.replace("$", "").replace(",", "")) <= 0.0 else "red")  
    print("Amount due: " + text)
    
task = BrowserTask(name = task, run_func = run, humanized_template = HUMAN_STR)
task.run()
task.commit_result()
