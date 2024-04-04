import pytest
import random
import mini_practicum
import assessMeTester_StringSimilarity
#TO RUN pytest --tb=short -s

def test_make_letter_frequency(capsys, monkeypatch, printFeedback=True):
        success = True
        assertMessage = "" ##Assert message

        ##MODIFY
        testerName = "test_make_letter_frequency"
        functionName = "make_letter_frequency"

        expected = {'a': 9805, 'b': 1746, 'c': 3004, 'd': 5470, 'e': 15398, 'f': 2382, 'g': 2944, 'h': 7890, 'i': 8636, 'j': 235, 'k': 1290, 'l': 5211, 'm': 2467, 'n': 8053, 'o': 9478, 'p': 1968, 'q': 220, 'r': 6612, 's': 7270, 't': 12202, 'u': 3978, 'v': 963, 'w': 2952, 'x': 176, 'y': 2584, 'z': 80}
          
        try:

            # invoke
            filename = 'data/alice.txt'
            result = mini_practicum.make_letter_frequency(filename)
          
            
            if result==None:
                 success=False
                 assertMessage="The function must return a value!"
                 raise
             
            # Part for string comparison!
            if result==expected:
                assert True
            else:
                success = False
                assertMessage=f"The {functionName} is not correct!\nExpected:{expected}"
                assertMessage+=f"\nReturned:{result}"
        except AttributeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except TypeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except AssertionError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except:
            pass
        
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "\n******************************************* "+testerName+ " *****************\n"
        feedback = feedback + "\033[93m"+ assertMessage+"\033[0m"+"\n\n"
        feedback = feedback + "\n\033[91m*******************************************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
        feedback = feedback + "\n\n\n"

        if printFeedback and len(assertMessage)>0:
            print(feedback)
        assert success,assertMessage


def test_print_letter_frequency(capsys, monkeypatch, printFeedback=True):

    inputs = {'a': 9805, 'b': 1746, 'c': 3004, 'd': 5470, 'e': 15398, 'f': 2382, 'g': 2944, 'h': 7890, 'i': 8636, 'j': 235, 'k': 1290, 'l': 5211, 'm': 2467, 'n': 8053, 'o': 9478, 'p': 1968, 'q': 220, 'r': 6612, 's': 7270, 't': 12202, 'u': 3978, 'v': 963, 'w': 2952, 'x': 176, 'y': 2584, 'z': 80}
    
    expected_output = """a 9805
b 1746
c 3004
d 5470
e 15398
f 2382
g 2944
h 7890
i 8636
j 235
k 1290
l 5211
m 2467
n 8053
o 9478
p 1968
q 220
r 6612
s 7270
t 12202
u 3978
v 963
w 2952
x 176
y 2584
z 80
Max letter is "e" with a count of 15398"""

    
    # Execute the function
      # Run the main function
    mini_practicum.print_letter_frequency(inputs)
    #Get the feedback
    captured = capsys.readouterr()

    similarity_threshold = 0.99  # Set your desired threshold here

    similarity_score = assessMeTester_StringSimilarity.string_similarity(expected_output, captured.out)

   
    if similarity_score >= similarity_threshold:
        feedback = "Strings are similar enough (score: {0:.2f}%). Test passed!".format(similarity_score * 100)
    else:
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "***************print_letter_frequency tester failed!***************"
        feedback = feedback+ "\nExpected:\n" +"\033[93m"+ expected_output+"\033[0m"+"\n\n"
        feedback = feedback + "\nCaptured:\n" +"\033[93m"+  captured.out +"\033[0m"
        feedback = feedback+ "\n\033[91m" ## RED START
        feedback = feedback + f"Strings are not similar enough (score: {similarity_score})"
        feedback = feedback + "\n***********************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
    # Use sys.stdout to write out the feedback message
    if(printFeedback):
        print(feedback + "\n")
  

    assert similarity_score >= similarity_threshold, f"Strings are not similar enough (score: {similarity_score})"



def test_FinalGrade(capsys, monkeypatch):
    
    totalPoints = 0

    ## CALL the testers, do not print, otherwise you will mess with some of the testers
  
    test_functions = [
        (test_make_letter_frequency,50),
        (test_print_letter_frequency,50)
    ]

    outputFeedbac = "############ TOTAL POINTS ###################\n"
    
    for function, point in test_functions:
        try:
            function(capsys,monkeypatch,False)
            outputFeedbac=outputFeedbac+f"PASS:{function.__name__}: {point}"+"\n"
            totalPoints += point
        except AssertionError:
            outputFeedbac=outputFeedbac+f"FAIL:{function.__name__}: {0}\n"
        
    
    print(outputFeedbac)
    print("Total points",totalPoints)
    
   # Define emoji ranges based on points
    if 90 <= totalPoints:
          emoji = "🌟✨💫💖😍🎉👏😎🥇🚀👏👏👏👏👏👏"
    elif 80 <= totalPoints < 90:
          emoji = "😃👍👌🙌🤗🥳😁👌👌👌👌"
    elif 70 <= totalPoints < 80:
          emoji = "😊😉❤️🌸🌼💝💓👌👌"
    elif 60 <= totalPoints < 70:
          emoji = "😐🤔😕😬😟😞"  # Thinking + Unamused + Disappointed
    else:
          emoji = "😢😥😭😩😖"
    print(emoji)
    assert True