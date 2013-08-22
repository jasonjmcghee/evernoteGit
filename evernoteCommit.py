from evernote.api.client import EvernoteClient
from evernote.edam.type import ttypes as Types
import sys

def makeNoteFromLastCommit(dev_token):
  client = EvernoteClient(token=dev_token, sandbox=True)
  userStore = client.get_user_store()
  user = userStore.getUser()
  #print user.username

  noteStore = client.get_note_store()
  notebooks = noteStore.listNotebooks()
  #for n in notebooks:
  #  print n.name

  note = Types.Note()
  note.title = sys.argv[1] + " " + sys.argv[2]
  note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
  content = ""
  content1 = ""
  content2 = ""
  parts = sys.argv[1:3]
  date = sys.argv[3:10]
  msg = sys.argv[10:]
  for s in parts:
    content += s+" "
  for s in date:
    content1 += s+" "
  for s in msg:
    content2 += s+" "
  note.content += '<en-note>'+ content + '<br/><br/>' + content1 + '<br/><br/>' + content2  +'</en-note>'
  note = noteStore.createNote(note)

dev_token = " your dev token "
makeNoteFromLastCommit(dev_token)
