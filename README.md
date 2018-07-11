# Rajastan_Hackathon_18
Smart Mirror


OpenCV Version: 3.4.1

STEPS:

   1:   In my case i simply un-installed and installed back opencv-python
        Before re-installation i had opencv-python-3.3.0.10. after re-install i got a newer version opencv-python-3.4.0.12

        pip3 uninstall opencv_python
        pip3 install opencv_python --user

        After typing these two commands you get latest version of OpenCV > 3.4
        
   2:   1 [compiler] sudo apt-get install build-essential
        2 [required] sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
        3 [optional] sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev       libjasper-dev libdc1394-22-dev
        
        These installs all the dependancies.
        


Sources/References:

https://www.youtube.com/redirect?v=v-XcmsYlzjA&event=video_description&q=https%3A%2F%2Fgithub.com%2FSadaival%2FHand-Gestures.git&redir_token=WFeQxFzm15ke1TFvJ8HIoJikVPJ8MTUzMTM3NjU2NUAxNTMxMjkwMTY1

I have used concept of Dilation and Blurring from this code.
I have used their HSV value of the skin colour.

I will update these section.



