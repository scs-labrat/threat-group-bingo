import random
import os
from colorama import init, Fore, Style
import pyfiglet

# Initialize colorama
init()

# List of MITRE ATT&CK techniques
mitre_attack_techniques = [
    "Reconnaissance: Active Scanning",
    "Reconnaissance: Gather Victim Host Information",
    "Reconnaissance: Gather Victim Identity Information",
    "Reconnaissance: Gather Victim Network Information",
    "Reconnaissance: Phishing for Information",
    "Reconnaissance: Search Open Technical Databases",
    "Resource Development: Acquire Infrastructure",
    "Resource Development: Compromise Infrastructure",
    "Resource Development: Develop Capabilities",
    "Resource Development: Establish Accounts",
    "Resource Development: Obtain Capabilities",
    "Resource Development: Stage Capabilities",
    "Initial Access: Drive-by Compromise",
    "Initial Access: Exploit Public-Facing Application",
    "Initial Access: Hardware Additions",
    "Initial Access: Phishing",
    "Initial Access: Supply Chain Compromise",
    "Initial Access: Trusted Relationship",
    "Execution: Command and Scripting Interpreter",
    "Execution: Command-Line Interface",
    "Execution: Exploitation for Client Execution",
    "Execution: Graphical User Interface",
    "Execution: InstallUtil",
    "Execution: PowerShell",
    "Execution: Remote Services",
    "Execution: Scheduled Task",
    "Execution: Scripting",
    "Execution: Service Execution",
    "Execution: Signed Binary Proxy Execution",
    "Execution: User Execution",
    "Execution: Windows Management Instrumentation",
    "Persistence: Account Manipulation",
    "Persistence: Boot or Logon Autostart Execution",
    "Persistence: Browser Extensions",
    "Persistence: Create Account",
    "Persistence: Create or Modify System Process",
    "Persistence: Hijack Execution Flow",
    "Persistence: Office Application Startup",
    "Persistence: Pre-OS Boot",
    "Persistence: Registry Run Keys / Start Folder",
    "Persistence: Scheduled Task",
    "Persistence: Server Software Component",
    "Persistence: Service Registry Permissions Weakness",
    "Persistence: Valid Accounts",
    "Privilege Escalation: Access Token Manipulation",
    "Privilege Escalation: Accessibility Features",
    "Privilege Escalation: AppCert DLLs",
    "Privilege Escalation: Bootkit",
    "Privilege Escalation: Bypass User Account Control",
    "Privilege Escalation: DLL Search Order Hijacking",
    "Privilege Escalation: Exploitation for Privilege Escalation",
    "Privilege Escalation: File System Permissions Weakness",
    "Privilege Escalation: Hooking",
    "Privilege Escalation: Kernel Modules and Extensions",
    "Privilege Escalation: New Service",
    "Privilege Escalation: Process Injection",
    "Privilege Escalation: Scheduled Task",
    "Privilege Escalation: Setuid and Setgid",
    "Privilege Escalation: Valid Accounts",
    "Defense Evasion: Access Token Manipulation",
    "Defense Evasion: BITS Jobs",
    "Defense Evasion: Clear Command History",
    "Defense Evasion: Cloud Service Dashboard",
    "Defense Evasion: Code Signing",
    "Defense Evasion: Compile After Delivery",
    "Defense Evasion: Component Firmware",
    "Defense Evasion: Control Panel Items",
    "Defense Evasion: Data Encoding",
    "Defense Evasion: Deobfuscate/Decode Files or Information",
    "Defense Evasion: Disabling Security Tools",
    "Defense Evasion: Downgrade Account",
    "Defense Evasion: Exploitation for Defense Evasion",
    "Defense Evasion: File Deletion",
    "Defense Evasion: File System Permissions Weakness",
    "Defense Evasion: Hidden Files and Directories",
    "Defense Evasion: Hidden Users",
    "Defense Evasion: Hidden Window",
    "Defense Evasion: Indicator Removal from Tools",
    "Defense Evasion: Indicator Removal on Host",
    "Defense Evasion: Indicator Removal on Host: Clear Windows Event Logs",
    "Defense Evasion: Indicator Removal on Host: File Deletion",
    "Defense Evasion: Indicator Removal on Host: File System Logical Offsets",
    "Defense Evasion: Indicator Removal on Host: Indirect Command Execution",
    "Defense Evasion: Indicator Blocking",
    "Defense Evasion: Indicator Removal from Tools",
    "Defense Evasion: Network Share Connection Removal",
    "Defense Evasion: Redundant Access",
    "Defense Evasion: Timestomp",
    "Defense Evasion: Valid Accounts",
    "Defense Evasion: Windows Event Logs",
    "Defense Evasion: Windows File Deletion",
    "Defense Evasion: Windows Registry Hives",
    "Defense Evasion: Windows Service",
    "Defense Evasion: Install Root Certificate",
    "Defense Evasion: Masquerading",
    "Defense Evasion: Modify Registry",
    "Defense Evasion: Network Share Connection Removal",
    "Defense Evasion: Obfuscated Files or Information",
    "Defense Evasion: Process Injection",
    "Defense Evasion: Redundant Access",
    "Defense Evasion: Re-enable Accounts",
    "Defense Evasion: Remote Access Software",
    "Defense Evasion: Rootkit",
    "Defense Evasion: Runtime Data Manipulation",
    "Defense Evasion: Scripting",
    "Defense Evasion: Software Packing",
    "Defense Evasion: Space after Filename",
    "Defense Evasion: Trusted Developer Utilities Proxy Execution",
    "Defense Evasion: Virtualization/Sandbox Evasion",
    "Defense Evasion: Web Service",
    "Credential Access: Account Manipulation",
    "Credential Access: Brute Force",
    "Credential Access: Credential Dumping",
    "Credential Access: Credentials in Files",
    "Credential Access: Credentials in Registry",
    "Credential Access: Exploitation for Credential Access",
    "Credential Access: Input Capture",
    "Credential Access: Kerberoasting",
    "Credential Access: Keychain",
    "Credential Access: Network Sniffing",
    "Credential Access: Password Guessing",
    "Credential Access: Private Keys",
    "Credential Access: Security Account Manager",
    "Credential Access: Steal or Forge Kerberos Tickets",
    "Credential Access: Steal Web Session Cookie",
    "Credential Access: Two-Factor Authentication Interception",
    "Credential Access: Unsecured Credentials",
    "Credential Access: Windows Credential Manager",
    "Credential Access: Windows Logon Session",
    "Discovery: Account Discovery",
    "Discovery: Application Window Discovery",
    "Discovery: Browser Bookmark Discovery",
    "Discovery: Cloud Service Discovery",
    "Discovery: Cloud Storage Object Discovery",
    "Discovery: Command and Scripting Interpreter",
    "Discovery: Data from Local System",
    "Discovery: Data from Network Shared Drive",
    "Discovery: Data from Removable Media",
    "Discovery: Email Collection",
    "Discovery: File and Directory Discovery",
    "Discovery: Network Service Scanning",
    "Discovery: Network Share Discovery",
    "Discovery: Password Policy Discovery",
    "Discovery: Permission Groups Discovery",
    "Discovery: Peripheral Device Discovery",
    "Discovery: Process Discovery",
    "Discovery: Remote System Discovery",
    "Discovery: Remote System Discovery: Domain Trust Discovery",
    "Discovery: Remote System Discovery: LANMAN Discovery",
    "Discovery: Remote System Discovery: Network Device Discovery",
    "Discovery: Remote System Discovery: Remote Desktop Protocol",
    "Discovery: Remote System Discovery: Remote Services",
    "Discovery: Remote System Discovery: Windows Remote Management",
    "Discovery: Security Software Discovery",
    "Discovery: System Information Discovery",
    "Discovery: System Network Configuration Discovery",
    "Discovery: System Network Connections Discovery",
    "Discovery: System Owner/User Discovery",
    "Discovery: System Service Discovery",
    "Discovery: System Time Discovery",
    "Discovery: User Discovery",
    "Lateral Movement: AppleScript",
    "Lateral Movement: Application Deployment Software",
    "Lateral Movement: Command-Line Interface",
    "Lateral Movement: Distributed Component Object Model",
    "Lateral Movement: Exploitation of Remote Services",
    "Lateral Movement: Logon Scripts",
    "Lateral Movement: Pass the Hash",
    "Lateral Movement: Pass the Ticket",
    "Lateral Movement: Remote Desktop Protocol",
    "Lateral Movement: Remote File Copy",
    "Lateral Movement: Remote Services",
    "Lateral Movement: Replication Through Removable Media",
    "Lateral Movement: SSH",
    "Lateral Movement: Windows Admin Shares",
    "Lateral Movement: Windows Remote Management",
    "Collection: Audio Capture",
    "Collection: Automated Collection",
    "Collection: Clipboard Data",
    "Collection: Data Staged",
    "Collection: Data from Local System",
    "Collection: Data from Network Shared Drive",
    "Collection: Data from Removable Media",
    "Collection: Email Collection",
    "Collection: Input Capture",
    "Collection: Screen Capture",
    "Collection: Video Capture",
    "Command and Control: Commonly Used Port",
    "Command and Control: Connection Proxy",
    "Command and Control: Custom Command and Control Protocol",
    "Command and Control: Data Encoding",
    "Command and Control: Data Obfuscation",
    "Command and Control: Domain Fronting",
    "Command and Control: Fallback Channels",
    "Command and Control: Multi-Stage Channels",
    "Command and Control: Non-Application Layer Protocol",
    "Command and Control: Protocol Tunneling",
    "Command and Control: Proxy",
    "Command and Control: Remote Access Software",
    "Command and Control: Remote File Copy",
    "Command and Control: Standard Application Layer Protocol",
    "Command and Control: Standard Cryptographic Protocol",
    "Command and Control: Standard Non-Application Layer Protocol",
    "Command and Control: Traffic Signaling",
    "Exfiltration: Automated Exfiltration",
    "Exfiltration: Data Compressed",
    "Exfiltration: Data Encrypted",
    "Exfiltration: Data Transfer Size Limits",
    "Exfiltration: Exfiltration Over Alternative Protocol",
    "Exfiltration: Exfiltration Over Command and Control Channel",
    "Exfiltration: Exfiltration Over Other Network Medium",
    "Exfiltration: Exfiltration Over Physical Medium",
    "Exfiltration: Scheduled Transfer",
    "Impact: Account Access Removal",
    "Impact: Account Hijacking",
    "Impact: Application Access Token",
    "Impact: Application Denial of Service",
    "Impact: Application Deployment Software",
    "Impact: Audio Capture",
    "Impact: Data Destruction",
    "Impact: Data Encrypted",
    "Impact: Data Manipulation",
    "Impact: Data Spoofing",
    "Impact: Denial of Service",
    "Impact: Disk Structure Wipe",
    "Impact: Disk Wipe",
    "Impact: Domain Generation Algorithms",
    "Impact: Endpoint Denial of Service",
    "Impact: Firmware Corruption",
    "Impact: Hardware Component Destruction",
    "Impact: Inhibit System Recovery",
    "Impact: Input Capture",
    "Impact: Loss of Control",
    "Impact: Loss of Productivity and Revenue",
    "Impact: Network Denial of Service",
    "Impact: Non-Compliance",
    "Impact: Physical Access",
    "Impact: Physical Destruction",
    "Impact: Resource Hijacking",
    "Impact: Service Stop",
    "Impact: System Firmware",
    "Impact: System Shutdown/Reboot",
    "Impact: Tamper with System Configuration",
    "Impact: Wireless Access Point Denial of Service"
]

drawn_techniques = []

def display_random_technique(techniques):
    if not techniques:
        print(Fore.RED + "No more techniques left." + Style.RESET_ALL)
        return False
    technique = random.choice(techniques)
    ascii_banner = pyfiglet.figlet_format("MITRE ATT&CK")
    technique_banner = pyfiglet.figlet_format(technique)
    print(Fore.GREEN + ascii_banner + Style.RESET_ALL)
    print(Fore.YELLOW + technique_banner + Style.RESET_ALL)
    drawn_techniques.append(technique)
    techniques.remove(technique)
    return True

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_drawn_techniques():
    print(Fore.CYAN + "Already Drawn Techniques:" + Style.RESET_ALL)
    for technique in drawn_techniques:
        print(Fore.MAGENTA + technique + Style.RESET_ALL)

def show_help():
    help_text = """
Preparation:
1. Go to https://mitre-attack.github.io/attack-navigator and click the select icon
2. In the menu that pops up select a threat group from the drop down menu
3. In technique controls click the score icon and assign a value of 3
4. In the layer controls click color setup and assign a preset
5. In layer controls click export and then the camera to create an svg file
6. Print this out and you're ready to play

Rules:
[+] Each player chooses an APT group and prints out their navigator heat map
[+] Some APTs have more TTPs than others, if a player has chosen one with only a few, good on them for choosing wisely.
[+] The host runs the program calling out a technique on each spin
[+] The first player to cross off all techniques of their APT is the winner
"""
    print(Fore.CYAN + help_text + Style.RESET_ALL)

def main():
    remaining_techniques = mitre_attack_techniques.copy()
    while True:
        clear_screen()
        ascii_banner = pyfiglet.figlet_format("D8RH8R'S THREAT GROUP BINGO", font="cosmic")
        print(Fore.GREEN + ascii_banner + Style.RESET_ALL)
        user_input = input(Fore.CYAN + "Press 's' to start the game, 'h' for help, or 'q' to exit: " + Style.RESET_ALL)
        if user_input.lower() == 'q':
            print(Fore.RED + "Exiting the program." + Style.RESET_ALL)
            break
        elif user_input.lower() == 'h':
            clear_screen()
            show_help()
            input(Fore.CYAN + "Press Enter to return to the main menu: " + Style.RESET_ALL)
        elif user_input.lower() == 's':
            while True:
                clear_screen()
                if not display_random_technique(remaining_techniques):
                    break
                user_input = input(Fore.CYAN + "Press Enter for another technique, 'p' to see previous techniques, or 'q' to exit: " + Style.RESET_ALL)
                if user_input.lower() == 'q':
                    print(Fore.RED + "Exiting the program." + Style.RESET_ALL)
                    break
                elif user_input.lower() == 'p':
                    clear_screen()
                    show_drawn_techniques()
                    input(Fore.CYAN + "Press Enter to continue: " + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()