import tkinter as tk
def my_wechat(MyFeeling,who,content):
    window = tk.Tk()
    window.title("Jingjing's WeChat")
    window.geometry("400x200+400+400")
    window.config(bg='white')
    tk.Label(window,
             text=MyFeeling,
             bg = "white",
             font=("Arial", 30)).pack()
    tk.Label(window,
             text=who,
             bg = "white",
             font=("Arial", 15)).pack()
    tk.Label(window,
             text=content,
             bg = "white",
             font=("Arial", 20)).pack()
    window.after(60,lambda: window.destroy())
    window.mainloop()
    
def main():
    win = tk.Tk()
    win.title('WeChat')
    win.geometry("400x200+400+400")
    win.config(bg='#95a48b')
    tk.Label(win,text="48 hours is up\nclick the button to log into WeChat.",bg ='#95a48b',font=("Times New Roman", 20), fg='white').pack()  
    tk.Button(win, text='Log in', command= win.destroy).pack()
    win.mainloop()

def final():
    w = tk.Tk()
    w.title('WeChat')
    w.geometry("400x200+400+400")
    w.config(bg='#95a48b')
    tk.Label(w,text="SO\nMANY\nMESSAGES\nAHHHHHHHHHH",bg ='#95a48b',font=("Times New Roman", 30), fg='white').pack()
    tk.Label(w,text="🤦🏻‍♀️",bg ='#95a48b',font=("Times New Roman", 50), fg='white').pack()
    w.mainloop()

main()

contents1 = ["Jingjing", "Why r u ignoring me", "U better reply me miss", "I'm so Saddddddd", "Congrats on your interview!", "You are officially a tutor!", "We have a training here that starts from 7.20,\n it's a three-day-training, \n1-2 hours a day,\n you can watch the recording at night", "Jingjing", "Did you take Math 3A or 6N?", "Sorry for disturbing you~ \n Do we have to take under 4 units of online classes for summer?", "Jingjing", "Girl,\n do you have any school photos taken abroad?", "Who", "Is", "ur", "physics", "teacher", "in high school", "???", "Jingjing", "R u the girl with the red hair?", "What is the course selection process?","Jingjing","!!!!", "where r u", "your brother won an award", "friend request from group chat","friend request from ruya","friend request from vivian","friend request from ID","Hiiiiii","friend request","What major r u","friend request","I'm a first year in UCI","friend request","what's the answer of this question?", "???", "JJ DUBZ", "Hey, where did u go"]
contents = contents1 + list(set(contents1))
whos = ["family\n******\n*  🥰   *\n*       *\n******\n", "friends\n******\n* 👫 *\n*       *\n******\n", "UCI freshmen\n******\n* 👩‍🎓 *\n*       *\n******\n", "CSSA coworkers\n******\n* 🐼 *\n*       *\n******\n", "HR\n******\n* 👩‍🏫 *\n*       *\n******\n"]
whos = 100 * whos
MyFeelings = ['😆','😁','😀','🙂','😕','🙁','️🥱','😣','😖','😫','😵‍💫']
MyF = []
for i in range(len(MyFeelings)):
    for j in range(7):
        MyF.append(MyFeelings[i])
for i in range(len(contents)):
    content = contents[i]
    who = whos[i]
    MyFeeling = MyF[i]
    my_wechat(MyFeeling,who,content)
final()
