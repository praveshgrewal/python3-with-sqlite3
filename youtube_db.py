
#code copy or learn from chai or code (hitesh choudhary) youtube channel



import sqlite3
con = sqlite3.connect('mydb.db')
coursor = con.cursor()

coursor.execute('''
    Create Table IF NOT EXISTS video(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
    )
''')

def list_video():
    coursor.execute("SELECT * FROM video")
    for row in coursor.fetchall():
        print(row)
       
def add_video(name, time):
    coursor.execute("INSERT INTO video (name, time) VALUES (?,?)", (name, time))
    con.commit()                                                                                                                                                            
    
def update_video(video_id, new_name, new_time):
    coursor.execute("UPDATE video SET name=?, time=? WHERE id=?", (new_name, new_time, video_id))
    con.commit()
                                   
def delete_video(video_id):
    coursor.execute("DELETE FROM video WHERE id = ?", (video_id,))
    con.commit()

def main():
    while True:
        print("\n Youtube Manager App with DB")
        print("1. List video")
        print("2. add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. exit")
        choice= input("Enter your choice: ")
        if choice == '1':
            list_video()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video id: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)                         
        elif choice == '4':
            video_id = input("Enter the video id: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("invalid input")                                                                                                                                                                   

    con.close()


if __name__ == '__main__':
    main()