from pyscript import when, display, document

@when("click", "#submit-btn")
def show_message(event):
    name = document.querySelector("#name").value
    age = document.querySelector("#age").value
    school = document.querySelector("#school").value

    document.querySelector("#output").innerText = ""

    message = f"""Student Profile:\nName:{name} \nAge:{age} \nSchool:\"{school}\"\nWelcome to ICT!\n"""

    display(message, target="output")

