import subprocess, os, platform

def isWindows():
    if platform.system() == "Windows":
        return True

    return False


def runCommand(command:str):
    subprocess.run(command.split(), check=True)


def main():
    userInput = input("which version would you want to run (node, python?)\t")
    userInput = userInput.lower()

    nodeCheck = ["node", "nodejs", "node.js", "node js"]
    pythonCheck = ["python", "python3", "py", "python 3"]

    if isWindows():
        python = "python"

    else:
        python = "python3"

    if userInput in nodeCheck:
        # change directory to node
        os.chdir("node")

        # check if node_modules is installed
        # if not install it
        if not os.path.exists("node/node_modules"):
            runCommand("npm install ")

        # this one speaks for itself lol 
        runCommand("node index.js")

    elif userInput in pythonCheck:
        os.chdir("python")
        runCommand(f"{python} run.py")


if __name__ == "__main__":
    try:
        main()
    
    except KeyboardInterrupt:
        if os.getcwd() != "node" or os.getcwd() != "python":
            pass

        os.chdir("../")