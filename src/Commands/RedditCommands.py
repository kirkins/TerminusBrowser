from debug import DEBUG
from Views.viewClass import View

from Frames.reddit.subredditFrame import SubredditFrame
from Frames.reddit.threadFrame import RedditThreadFrame

def redditCommands(cmd, uvm):
    cmd = cmd.split()

    if cmd[0] in ('sub', 'subreddit'):
        DEBUG('executing subreddit command')
        subreddit(uvm, cmd[1], cmd[2] if len(cmd) == 3 else "")
    elif cmd[0] in ('p', 'post'):
        DEBUG('executing post command')
        post(uvm, cmd[1], cmd[2])

def subreddit(uvm, subString, token):
    DEBUG('Executing subreddit command')
    try:
        setattr(uvm.currFocusView, 'frame', SubredditFrame(subString, token, uvm))
        uvm.currFocusView.updateHistory(SubredditFrame.SubredditFrameFactory, [subString, token, uvm])
    except:
        DEBUG(f'Error connecting to subreddit {subString}, does it exist?')

def post(uvm, subString, postNumber):
    DEBUG('Executing post command')
    uvm.currFocusView.updateHistory(RedditThreadFrame.RedditThreadFrameFactory, [subString, postNumber, uvm])
    setattr(uvm.currFocusView, 'frame', RedditThreadFrame(subString, postNumber, uvm))