# frasierML
experimenting with ML, using GPT-2 and TensorFlow, using the hit TV show Frasier as a theme

### credits
- jared pettitt
- celeste clark jewett  

### uses
- Frasier scripts from KACL780.net
- images from seasons 1, 3, and 5 of hit TV show Frasier
- "Train a GPT-2 Text-Generating Model w/ GPU For Free"

### part 1
train a GPT-2 model on a corpus of the scripts of every episode of hit TV show Frasier

#### usage
- navigate to https://colab.research.google.com/drive/1Z63jvkBRVWnm5yFTL3GpGr3AqCg3hsKT
- in part1/corpus, run TextScraper.py to steal the scripts of every episode of frasier from KACL780.net
  - you don't actually need to do this though, the output is already in part1/corpus/out/alleps.txt
- go through the steps in the colab notebook
- when uploading the text file, upload alleps.txt

#### output examples
```

Scene 2  Caf Nervosa.
Frasier and Niles are sitting at a table.  
Outside, the street lights are out.

  Niles: We had the most fantastic time last night.  I can't wait to get 
         back to it.  Roz and I have been planning to go out again.
Frasier: I can't wait to get back to it. [to Niles] Oh, Niles.  
         You were so good last night.  You were perfect!  You were perfect 
         in bed.  I can't wait to get back to it.
  Niles: What are you talking about?  I'm fine.  I can't wait.  I can't wait.  
         I love you.  I love you.  I love you.  I love you.

Niles kisses Frasier on the cheek.

  Niles: I love you.
Frasier: I love you.  I love you

```
```
CUT TO: the bathroom.  Daphne is standing in front of a toilet 
with a man in a bathrobe.

 Daphne: [v.o., then] Oh, dear God!  You're the one who made me do this.  
         I can't even wash myself.  I just want to go and curl up on the 
         toilet and cry my eyes out.
    Man: [o.s.] I'm sorry, Daphne.  I can't say this.
 Daphne: [nervous] Oh, that's alright.  You're so sweet.  You're so sweet.  
         I can't believe I'm speaking to you.
    Man: [o.s.] I'm sorry, Daph.  I can't say anything.
 Daphne: [nervously] Oh, come on, it's alright.  I'm just so nervous.  
         [to the bathroom stall] Oh, dear God!  This is awful.  I want to get out of 
         Here.
```
```
ACT TWO]

She leaves.  Frasier bursts out laughing.

Flashback: dark comedy.  Frasier finds herself in the same 
situation as when she left, only this time 
         she's in an isolated room with a curtain and 
         the only lights are the ones in the room that surround 
         her.

 Frasier: Frasier, if this room was isolated then it wouldn't have 
         been dark comedy.  

Frasier sits, fighting with his mind.

 Frasier: All right, now listen, I realize that all of this is just a little  
         bit crude, but there are some truths I've learned through the years.  
         No matter how hard you try to hide it, the words "I don't 
         care," "I don't care," "I don't care" stick to you.  

```

###part 2
