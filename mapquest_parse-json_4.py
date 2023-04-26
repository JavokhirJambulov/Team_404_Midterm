import urllib.parse
import requests
import openai

openai.api_key = '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'
messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]

main_api = "https://www.mapquestapi.com/directions/v2/route?"

key = "LiK0g4cAuVKdQX7nkNGbVCFd4XIjKzNT"
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
        message = "Give me 5 best hotels in " + dest + " Do not display 'Sure, here are the 5 best hotels in Incheon:'"
        if message:
            messages.append(
                {"role": "user", "content": message},)
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
        reply = chat.choices[0].message.content
        print(f" {reply}")
        messages.append({"role": "assistant", "content": reply})
        print("************************************************************************")
        message = "Give me gas station location in  the route from" + orig +" to" + dest + " Do not display the initial message of the chatgpt response "
        if message:
            messages.append(
                {"role": "user", "content": message},
        )
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
        reply = chat.choices[0].message.content
        print(f"{reply}")
        messages.append({"role": "assistant", "content": reply})
        print("************************************************************************")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
    
    