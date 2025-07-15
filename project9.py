import random
import time

password = "ammar@1#2$3"
password1 = input('Enter your password: ')

if password1 == password:
    print("Your password is correct")

    while True:
        OTP = [1,2,3,4,5,6,7,8,9]
        OTP_Pass = random.sample(OTP, 5)
        number = int(''.join(map(str, OTP_Pass)))
        print(f"\nYour OTP is: {number}")
        print("Note: OTP will expire in 10 seconds\n")

        start_time = time.time()
        try:
            OTP_check = int(input("Enter your OTP: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        time_taken = time.time() - start_time

        if time_taken > 10:
            print("⏰ OTP expired!")
            retry = input("Do you want to regenerate OTP? (yes/no): ").lower()
            if retry == "yes":
                continue
            else:
                print("❌ Exiting login process.")
                break

        elif OTP_check == number:
            print("✅ You are successfully logged in!")
            break
        else:
            print("❌ Your OTP is incorrect.")
            break
else:
    print("❌ Your password is incorrect.")



