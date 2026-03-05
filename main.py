import time

# 🛡️ FUNCTIONS SECTION
def run_system_scanner():
    """Simulates a system vulnerability scan"""
    print("\n[+] Initializing system scan...")
    time.sleep(3)  # Realistic delay for the scan effect
    print("[+] Scan completed. No threats detected!\n")

def cyber_shield_system():
    print("=== CYBER-SHIELD SECURITY SYSTEM ACTIVATED ===")

    # 1. User Information Gathering
    profession = input("Enter your profession: ")
    print(f"Verified: {profession} is a critical role.\n")

    # 2. Blacklist and Login Verification
    blacklist = ["hacker01", "shumtaka", "virus_chi"]
    username = input("Enter Username: ")

    if username in blacklist:
        print("[-] ACCESS DENIED! You are in the blacklist.")
        return # Terminate the program for blacklisted users
    
    # 3. Password Security and Retry Loop
    while True:
        password = input("Enter System Password (default: 12345): ")
        if password == "12345":
            print("[+] Access Granted! Welcome back.")
            break
        else:
            print("[-] Incorrect Password! Please try again.")

    # 4. Age and Access Level Verification
    age = int(input("\nEnter your age: "))
    if age < 15:
        print("[-] Access restricted due to age safety policies.")
        return

    role = input("Enter your role (admin/director/guest): ").lower()
    if role == "admin" or role == "director":
        print("[>>>] Full Administrative privileges granted.")
    elif role == "guest":
        print("[>] Read-only access granted.")
    else:
        print("[-] Standard access granted.")

    # 5. Password Strength Validation
    new_password = input("\nCreate a new secure password: ")
    if len(new_password) < 8:
        print("[-] Error! Password too short. Use at least 8 characters.")
    else:
        print("[+] Password updated successfully! Strong security selected.")

    # 6. Quarantine and IP Blocking (Lists & Loops)
    quarantine_list = []
    suspicious_person = input("\nEnter name of suspicious user: ")
    quarantine_list.append(suspicious_person)
    print(f"[*] {suspicious_person} has been moved to quarantine: {quarantine_list}")

    malicious_ips = ["192.168.1.50", "10.0.0.99", "172.16.0.5"]
    print("\nDisconnecting malicious IP addresses from the network:")
    for ip in malicious_ips:
        print(f" [!] Terminating connection: {ip}")
        time.sleep(0.5)

    # 7. Database Checks (Dictionaries)
    user_database = {"botir": "danger", "nodir": "trusted"}
    check_user = input("\nCheck user status in database: ").lower()
    if check_user in user_database:
        if user_database[check_user] == "danger":
            print("[!!!] WARNING! This person is flagged as DANGEROUS!")
        else:
            print("[+] This user is TRUSTED.")
    else:
        print("[?] User not found in database.")

    # 8. Triggering the Vulnerability Scanner
    command = input("\nType 'start' to run the vulnerability scanner: ")
    if command == "start":
        run_system_scanner()

    print("=== System Shutdown. Stay Secure! ===")

# Entry point of the program
if __name__ == "__main__":
    cyber_shield_system()
