# Buffer Overflow Binary Patching

Description: This project demonstrates how buffer overflow vulnerabilities can still be exploited through binary patching. Even when basic secure coding practices like limiting input size with scanf("%31s", buffer) are used, attackers can modify the compiled binary to remove these input limits and potentially exploit the vulnerability.

How It Works: The code allows you to:

    Search for specific byte expressions in a binary file.
    View the bytes at a specific position.
    Modify the file by patching certain bytes, simulating a potential exploit.

Use Case: This tool is intended to showcase the concept of binary patching and buffer overflow vulnerabilities. It highlights how an attacker could alter a compiled binary to bypass input size checks and exploit vulnerabilities that would otherwise be mitigated by safe programming practices.

Getting Started:

    Clone this repository to your local machine.
    Ensure you have Python installed.
    Run the script to explore buffer overflow vulnerabilities in binary files.
