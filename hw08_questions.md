# HW08: It's In Your Genes

## Instructions

**Replace each `**Replace This With Your Answer**` with your answer**

---
## SECTION 1

Answer the following reflection prompts:

1.a. In just a _single_ sentence, summarize what you see as the top three primary takeaways that you have gained from 
reading these two articles.

```
   I learned that Google values problem‑solving over grades, looks for people with leadership and humility, 
   and cares more about how you think and learn than where you went to school.
```

1.b. Briefly describe the teamwork skills Google values that have been a part of this class.

```
   *Google values teamwork skills like stepping up to lead when needed, stepping back to let others lead, 
   and working together to solve problems—skills we practiced in group projects and discussions.
```

1.c. Do you think that what Laszlo Bock says about the importance of grades might be a more widely held perspective? 
How do you think this relates to you? Explain.

```
    Yes, I think companies now care less about grades and more about real skills. Knowing this helps me 
    to  focus on soft skills that are important in the workplace, as I prepare to get a good job in the future.

1.d. What are the five qualities Google looks for in a new hire and why do you think these are the most valuable 
qualities to Google in particular?

```
   Google looks for general cognitive ability, emergent leadership, humility, ownership, and expertise; 
   these matter because Google wants people who can think quickly, lead when needed, collaborate well,
   take responsibility, and keep learning in a fast‑changing environment.
```


1.e. Laszlo Bock says that most people "don't put enough thought into why they’re going (to college), and what they 
want to get out of it." The implication is that by thinking more and by being more strategic and explicit about what 
you want to get from college, you will gain far more. Reflect on the level of explicitly strategic thinking that you 
have given to what you want to get from college, and how much more strategic thinking you plan to do about this after 
reading this article.

```
   Before reading the article, I had not thought very deeply about what I want to get from college apart from the degree,
   but now I realize I need to be more intentional about choosing classes, building skills, 
   and focusing on what will help me grow in the long run.
```

1.f. If you got an offer, would you want to work at Google? Explain. Note: If you think Google is out of reach for you, 
think again, Katie Panciera (2005), worked at Google for 5 years before deciding she wanted to be a professor. 
Anne Otieno (2018), Emely Alfaro Zavala (2020), Giorgi Lomia (2020) and Elaheh Jamali (2020) are all graduates of this 
department who got their first jobs at Google and who still work there. You should connect with them on [LinkedIn](https://www.linkedin.com/search/results/people/?currentCompany=%5B%221441%22%5D&keywords=%22berea%20college%22&origin=FACETED_SEARCH&schoolFilter=%5B%2226240%22%5D&sid=XJp)!

```
    Yes, I would take the job if Google offered it to me because it is a great opportunity to learn and grow,
    but Google would not be my first priority since I have other interests and career goals I want to explore first.
```

1.g. Regardless of the company you end up working for, what is your dream job?

```
   My dream job is to become a data analyst or data scientist, because I enjoy working with data, finding patterns, 
   and using information to solve real problems and help people make better decisions.
```

_Return to the Google Doc and continue the assignment._

---

## SECTION 2

2.a. Briefly explain what are the key things you learned from the two articles on resumes about how to build an 
effective resume that is screened by a human or a robot.

```
   I learned that a good resume should be simple, and easy for the robot to read. For resumes that will be reviewd by
    humans, you should try to keep it short and straight to the point, and make sure it has no errors.
```

The National Association of Colleges and Employers conducts an annual survey of thousands of employers and determined 
the following: NACE’s Job Outlook 2020 survey found that beyond a strong GPA, problem-solving skills and the ability 
to work as part of a team are the most important resume attributes to employers. More than 91 percent of employer 
respondents are seeking the former in the candidates they are recruiting, and more than 86 percent want proof of the 
latter.

2.b. From [this article](https://www.naceweb.org/talent-acquisition/candidate-selection/what-are-employers-looking-for-when-reviewing-college-students-resumes), 
discuss your reaction to the chart _Figure 1: Attributes Employers Seek on a Candidate’s Resume_ from this link. 
Is there anything that you find interesting, surprising, or counter to your expectations?

```
   What stood out to me in the NACE chart is how highly employers rank problem‑solving skills and teamwork.
   More than 91% of employers want to see problem‑solving ability, and more than 86% want proof that the candidate
   can work well on a team.  I was also surprised that entrepreneurial skills were so low on the list, at only 21.8%, 
    because I expected companies to value creativity and entrepreneurial thinking much more.
```

_Return to the Google Doc and continue the assignment._

---

## SECTION 3

3.a. How much did this assignment help you with your resume? Did you already have a resume or did you make a new one? 
     If you had a resume already, how much did this help you to update it? Explain what you did. Be sure you upload 
     your resume when you complete this assignment.

```
   This assignment helped me make a few minor but important improvements to my resume.
   I already had a resume before doing this assignment, but reviewing the guidelines helped me clean it up and make it
   more professional. I made small updates such as adjusting the formatting to keep everything consistent, checking 
   that my skills were clearly listed, and making sure my work experience bullets started with strong action verbs. 
   I also confirmed that my contact information, LinkedIn link, education section, GPA, and relevant coursework 
   were all clearly displayed at the top in the correct format. I added a bit more detail to some job descriptions 
   to make my responsibilities clearer and more measurable, but overall the changes were small.
```

_Return to the Google Doc and continue the assignment._

___

## SECTION 4

Each numbered item below is one of the functions in the **hw08_genes.py** file. Read the descriptions provided below, 
then determine what the function should return as an output. 

4.a. **Function 1**: `is_nucleotide()` 
   
   Tests a string to see if it is a valid DNA strand. 
   A valid strand consists solely of the 4 nucleotides: `A`, `C`, `G`, and `T`

```
   What should the following calls to `is_nucleotide()` return?
      a. is_nucleotide(“TAG”): **Replace This With Your Answer**
      b. is_nucleotide(“CAB”): **Replace This With Your Answer**  
```

4.b. **Function 2**: `complement_strand()`

   Determines the complementary sequence of a valid DNA strand given that:
   ```    
      T pairs with A
      A pairs with T
      C pairs with G
      G pairs with C
   ```

   _Example: The strand `TACG` would produce a `ATGC`._

```
   What do the following calls to `complement_strand()` return?   
      a. complement_strand("CAT"): **Replace This With Your Answer**   
      b. complement_strand("GTG"): **Replace This With Your Answer**  
```

4.c. **Function 3**: `mRNA()`

   Though this is a bit of a simplification, we will assume that the mRNA of a DNA sequence will take the complement 
   strand of the DNA sequence as input and will replace each occurrence of the nucleotide T with the nucleotide U.  
   
   _Example: the complement strand `TACG` would produce `UACG`._

```
   What do the following calls to `mRNA()` return?
       a. mRNA("CAT"): **Replace This With Your Answer**
       b. mRNA("TTA"): **Replace This With Your Answer**
```

4.d. **Function 4**: `chunk_amino_acid()`

   This function takes your sequence as a string and converts it to a list, where each element of the list is the 
   next three letters from the original string. If there are 1 or 2 extra letters at the end, they are stripped 
   entirely from the sequence.

   _Example: the input sequence `CAUGACU` would output [“CAU”, “GAC”]._

```
   What do the following calls to `chunk_amino_acid()` return?
       a. chunk_amino_acid(“CAGUACGAT”): **Replace This With Your Answer**
       b. chunk_amino_acid(“CCGUGGGATAT”): **Replace This With Your Answer** 
```

4.e. **Function 5:** `translate_amino_acid()`

   This function expects a three character string as a parameter and returns the corresponding single character 
   amino acid. A dictionary is used to map the input parameters to the expected output. 

   _Example: the input sequence `GAA` would output the value `E`._

   **This function is already written for you. DO NOT modify this function.** You'll need to read the already-written code to answer the following questions:

```
   What do the following calls to `translate_amino_acid()` return?
      a. translate_amino_acid(“GCA”): **Replace This With Your Answer**
      b. translate_amino_acid(“CACAUU”): **Replace This With Your Answer**
```

4.f. **Function 6**: `sequence_gene()`

   Takes a sequence of nucleotides and will utilize _all_ of the above functions to return the 
   corresponding amino acid sequence. You should test this function as well, but because all other functions 
   must be written (and correct) before you can understand this function fully, I recommend waiting until the very 
   end to do this section. 

   _Example: the input string `CGTAGGCAT` would output the value `ASV`._

   **This function is already written for you. DO NOT modify this function**

```
   What do the following calls to `sequence_gene()` return?
      a. sequence_gene(“GCA”): **Replace This With Your Answer**
      b. sequence_gene(“CACAUU”): **Replace This With Your Answer**   
```

___

## SECTION 5

One way of thinking about functions is to imagine them as a black box, where you can only see the inputs and outputs, 
but not what is happening inside the function. We tried to make you think this way about your functions by having you 
write the test cases before writing the functions. 

5.a. Which did you write first, the _functions_ or the _test cases_?

```
   **Replace This With Your Answer**
```

5.b. Had you done the alternative, do you think this assignment would have been easier or harder?

```
   **Replace This With Your Answer**
```

5.c. This is easily the largest body of code you’ve encountered in this course. What was challenging about this 
assignment? How could you mitigate those challenges in future assignments?

```
   **Replace This With Your Answer**
```