import os,random,subprocess

#default path
path = "/root/Videos/television series/FRIENDS/"
#to list all the directory
directories = os.listdir(path)

#list all the folders present in the directory
print directories

#choose random season from the directory
selected_directory = random.choice(directories)

print "The selected season is:" , selected_directory

#to select the random video from the selected_directory
selected_episode = os.listdir("/root/Videos/television series/FRIENDS/" + selected_directory)

random_selected_episode = random.choice(selected_episode)

#selected_episode = random.choice("/root/Videos/television series/FRIENDS/" + selected_directory )

print "Selected episode is:" , random_selected_episode

print "Playing " , random_selected_episode , ".....!"

p = subprocess.Popen(["/usr/bin/vlc",path + selected_directory +"/"+random_selected_episode])
