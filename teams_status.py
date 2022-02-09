# Helper class with functions parse the Teams log file and assign an RGB value to the current status.

class teamsStatus():

    def __init__(self, 
                Available = 'Added Available',
                Busy = 'Added Busy',
                DoNotDisturb = 'Added DoNotDisturb',
                BeRightBack = 'Added BeRightBack',
                OnThePhone = "Added OnThePhone",
                Presenting = "Added Presenting",
                InAMeeting = "Added InAMeeting",
                Away = 'Added Away',
                Offline = 'Offline',
                green_hue = (0,255,0),
                yellow_hue = (255,255,0),
                red_hue = (255,0,0),
                off_hue = (0,0,0),
                filepath = "C:\\Users\\username\\AppData\\Roaming\\Microsoft\\Teams"
                ):

        # Set the default status's based on MSFT Teams log file.
        # Note, I've made the status keywords editable when instantiating the 
        # class in the event Teams changes them in the future or if you would like
        # to adjust the hue's of each status color.
        self.Available = Available
        self.Busy = Busy
        self.DoNotDisturb = DoNotDisturb
        self.BeRightBack = BeRightBack
        self.OnThePhone = OnThePhone
        self.Presenting = Presenting
        self.InAMeeting = InAMeeting
        self.Away = Away
        self.Offline = Offline
        
        # Initialize a last known status variable and colors for the lights 
        # (also editable if want to try a different hue).
        self.last_known_status = None
        self.green = green_hue
        self.yellow = yellow_hue
        self.red = red_hue
        self.off = off_hue

        # Intialize the filepath variable
        self.filepath = filepath
        

    def get_status(self):
        # Create a list of the status's to easily loop through and find a matching value
        status = [self.Available,
                self.Busy,
                self.DoNotDisturb,
                self.BeRightBack,
                self.Away,
                self.InAMeeting,
                self.OnThePhone,
                self.Presenting,
                self.Offline]

        # Look for this string in the MSFT Teams log file
        indicator = 'StatusIndicatorStateService: Added '

        # Open the log file
        log_file = open(f"{self.filepath}\\logs.txt", "r")

        # Create an index variable and list to store lines
        index = 0
        line_list = []

        # Loop through the file line by line
        for line in log_file:
            # Find
            if indicator in line:
                # Increment the index every line that matches the indicator 
                # variable & append that to the list of lines	
                index += 1
                line_list.append(line)

        # Store the last instance of the line containing the indicator
        line = line_list[index-1]

        # Loop through list of possible status's, if the last instance indicator 
        # finds a match, return that status
        for i in range(len(status)):
            if line.__contains__(status[i]):
                return status[i]
            else:
                pass

        # closing text file	
        log_file.close()

    def status_color(self, status):
        # Light control logic based on the status.
        # Returns formatted string "R,G,B" & the color in string format. 
        # DO NOT update the return values here...use custom_return dictionary in teams_light.py
        
        # This is a special condition when the Teams log file overflows and the indicator line is no longer present.
        if status == None: # Do not move or remove this condition.
            status = self.last_known_status
        if status == self.Available:
            self.last_known_status = status
            return self.green, "Green"      
        if status == self.DoNotDisturb or status == self.Busy or status == self.InAMeeting or status == self.OnThePhone or status == self.Presenting:
            self.last_known_status = status
            return self.red, "Red"          
        if status == self.Offline:
            self.last_known_status = status
            return self.off, "Off"
        else:
            self.last_known_status = status
            return self.yellow, "Yellow"

