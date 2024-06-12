#!/usr/bin/env python3
from dataclasses import dataclass

import draganddrop as dnd

from nicegui import ui


@dataclass
class ToDo:
    title: str


def handle_drop(todo: ToDo, location: str):
    ui.notify(f'"{todo.title}" is now in {location}')


with ui.row():
    # with dnd.column('Course Outline', on_drop=handle_drop):
    #     dnd.card(ToDo(
    #         'Introduction to our course: Overview of the course, including objectives, structure, and what students can expect to gain.'))
    #     dnd.card(ToDo(
    #         'Purpose of our course - Employable: Explaining the primary goal of the course, which is to make students employable by equipping them with industry-relevant skills.'))
    #     dnd.card(ToDo(
    #         'Our approach: Detailed description of our teaching methods, including interactive sessions, hands-on projects, and continuous assessments to ensure thorough understanding and skill development.'))
    #     dnd.card(ToDo(
    #         'Possible approaches - Top down and bottom up (ideally we should take both). Let\'s discuss more on this later: Introduction to different learning strategies and the importance of combining them for a comprehensive learning experience.'))
    #     dnd.card(ToDo(
    #         'What should we see in our minds - Top down, another name for samkalp: Discussing the importance of having a clear vision and goals (samkalp) to guide the learning process.'))
    #     dnd.card(ToDo(
    #         'My understanding of the market and the fields and subfields there are: Analysis of the current job market, including high-demand fields and emerging subfields that offer lucrative career opportunities.'))
    #     dnd.card(ToDo(
    #         'It may look like we all are doing it together, but this is an individual journey and I can facilitate, but you have to walk: Emphasizing the importance of individual effort, personal responsibility, and self-paced learning within the course structure.'))
    #
    # with dnd.column('Goals and Ideal Scenarios', on_drop=handle_drop):
    #     dnd.card(ToDo(
    #         'Let\'s try to imagine the ideal scenario and let\'s chase it. Ideally by midway through this course, you should be giving interviews, much better if you got jobs midway and you left: Encouraging students to set ambitious goals, such as securing job interviews and employment opportunities by the middle of the course.'))
    #
    # with dnd.column('Employability Skills', on_drop=handle_drop):
    #     dnd.card(ToDo(
    #         'What constitutes employability: Overview of the key skills and attributes that make a candidate attractive to employers.'))
    #     dnd.card(ToDo(
    #         '1) Good CV: Tips on writing an effective CV that highlights relevant skills and experiences. Emphasize the importance of tailoring your CV to match job requirements. Example: "I am good at chess, so make me a cricketer" makes no sense. How to tailor your CV to match job requirements.'))
    #     dnd.card(ToDo(
    #         '2) Bit of coding skills (in case for first round screening): Importance of having basic coding skills to pass initial technical screenings. Tips on acquiring and demonstrating these skills.'))
    #     dnd.card(ToDo(
    #         '3) Project: The importance of having a personal or group project to showcase practical application of skills. How to choose a project topic and document your work.'))
    #     dnd.card(ToDo(
    #         '4) Host the project so that you can show it to the interviewer: Steps to host your project online, including platforms to use and how to make your project easily accessible to potential employers.'))
    #     dnd.card(ToDo(
    #         '5) Good interview: Preparing for job interviews, including common questions, behavioral interview techniques, and tips for making a positive impression.'))
    #
    # with dnd.column('Career Planning', on_drop=handle_drop):
    #     dnd.card(ToDo(
    #         'So, what skills should I learn? Can I become an international cricketer now? Ideally, choose skills that you are natural at. Cook and coder both make money, but if you don\'t know what you have natural talent in, that is a bigger concern: Guidance on identifying your strengths and choosing a career path that aligns with your natural talents and interests.'))
    #     dnd.card(ToDo(
    #         'Probably the most important part that is overlooked: go to LinkedIn, Naukri: Importance of using professional networks and job portals to understand market demands, network with professionals, and find job opportunities. Tips on how to effectively use these platforms.'))
    #
    #


    with dnd.column('Overview', on_drop=handle_drop):
        dnd.card(ToDo('Where do I fit in (Market Understanding)? '))
        dnd.card(ToDo('Lets fix our goal'))
        dnd.card(ToDo('Where do I have my natural talent'))
        dnd.card(ToDo('What career option should I choose (Data Analyst, Data Scientist, Data Engineer'))
        dnd.card(ToDo('What career option should I choose (Web development, learn basic python  )'))
        dnd.card(ToDo('Who will be my employer, What type of jobs (domains) I will be applying after learning this course '))
        dnd.card(ToDo('What skill sets are they looking out for'))
        # dnd.card(ToDo('Possible approaches - Top down and bottom up   (ideally  we should take both). lets discuss more on this later'))
        # dnd.card(ToDo('What should we see in  our minds Top down another name for samkalp'  ))
        dnd.card(ToDo('For an ideal scenario, by mid way or 3/4 through this course , what should I do now to start giving interviews'))
        dnd.card(ToDo('What constitutes employability :'))


        dnd.card(ToDo('0) what are the available jobs in the market, market knowledge,  Probably the most important part that is overlooked, go to linkedin, naukiri understand market fields and subfields that are present'))
        dnd.card(ToDo('1) Good cv, But to write a good cv ,you should write those skills that the employer is looking for, look ou if you have natural talent some where,'
                      'if you dont know what you have natural talent lets explore to find out'))
        dnd.card(ToDo('2)Coding skils (incase for first round screening)'))
        dnd.card(ToDo('3)Project'))
        dnd.card(ToDo('4)host the project that you want to show to interviewer'))
        dnd.card(ToDo('5)Interview preparation  (Looking into general interview questions that are being asked )'))
        dnd.card(ToDo('6)Applying for jobs'))

    # dnd.card(ToDo('It may look like we all are doing it together, but  this is an individual journey and I can facilitate, but you have to walk'))

    with dnd.column('Fitting into markets requirement', on_drop=handle_drop):
        dnd.card(ToDo('Todolist'))
        dnd.card(ToDo('Doing'))
        dnd.card(ToDo('Done'))
        dnd.card(ToDo('skills required, Basic Python, git'))


    with dnd.column('CV', on_drop=handle_drop):
        dnd.card(ToDo('Todolist'))
        dnd.card(ToDo('Making cv incorporating the skills required'))
        dnd.card(ToDo('Doing'))
        dnd.card(ToDo('Done'))

    with dnd.column('Coding skills ', on_drop=handle_drop):
        dnd.card(ToDo('Todolist'))
        dnd.card(ToDo('Practice coding'))
        dnd.card(ToDo('For advanced practice Data Structures and Algorithms'))
        dnd.card(ToDo('Doing'))
        dnd.card(ToDo('Done'))

    with dnd.column('project ', on_drop=handle_drop):
        dnd.card(ToDo('Todolist'))
        dnd.card(ToDo('Finding the project that is useful and valued in the market , find from  job descriptions'))
        dnd.card(ToDo('Doing'))
        dnd.card(ToDo('Done'))

    with dnd.column('Hosting the project ', on_drop=handle_drop):
        dnd.card(ToDo('Todolist'))
        dnd.card(ToDo('Little web development to host the project (Displaying your skills are equally important as much as having them)'))
        dnd.card(ToDo('Doing'))
        dnd.card(ToDo('Done'))

    with dnd.column('Interview Preparation', on_drop=handle_drop):
        dnd.card(ToDo('Todolist'))
        dnd.card(ToDo('Find questions that are regularly asked'))
        dnd.card(ToDo('Doing'))
        dnd.card(ToDo('Done'))

    with dnd.column('Applying for jobs ', on_drop=handle_drop):
        dnd.card(ToDo('Todolist'))
        dnd.card(ToDo('Applying the jobs that suit you and around them '))
        dnd.card(ToDo('After applying the revert times vary from 15 days to 1 month '))
        dnd.card(ToDo('Ability to handle rejection and being consistent '))
        dnd.card(ToDo('Doing'))
        dnd.card(ToDo('Done'))


    with dnd.column('Python Syllabus', on_drop=handle_drop):
        dnd.card(ToDo('Todolist'))
        dnd.card(ToDo('Lists'))
        dnd.card(ToDo('Tuples'))
        dnd.card(ToDo('Dictionary'))
        dnd.card(ToDo('Sets'))
        dnd.card(ToDo('Strings'))
        dnd.card(ToDo('Collections'))
        dnd.card(ToDo('Itertools'))
        dnd.card(ToDo('Lambda'))
        dnd.card(ToDo('Functions'))
        dnd.card(ToDo('Exceptions And Errors'))
        dnd.card(ToDo('Logging'))
        dnd.card(ToDo('JSON'))
        dnd.card(ToDo('Random'))
        dnd.card(ToDo('Numbers'))
        dnd.card(ToDo('Decorators'))
        dnd.card(ToDo('Generators'))
        dnd.card(ToDo('Threading vs Multiprocessing'))
        dnd.card(ToDo('Multithreading'))
        dnd.card(ToDo('Multiprocessing'))
        dnd.card(ToDo('Function arguments'))
        dnd.card(ToDo('Asterisk operator'))
        dnd.card(ToDo('Shallow vs Deep Copying'))
        dnd.card(ToDo('Context Managers'))
        dnd.card(ToDo('Doing'))
        dnd.card(ToDo('Done'))

    with dnd.column('Machine Learning', on_drop=handle_drop):
        dnd.card(ToDo('KNN(K Nearest Neighbors)'))
        dnd.card(ToDo('Linear Regression'))
        dnd.card(ToDo('Logistic Regression'))
        dnd.card(ToDo('Linear and Logistic Regression Refactoring'))
        dnd.card(ToDo('Naive Bayes'))
        dnd.card(ToDo('Perceptron'))
        dnd.card(ToDo('SVM(Support Vector Machine)'))
        dnd.card(ToDo('Decision Tree'))
        dnd.card(ToDo('Random Forest'))
        dnd.card(ToDo('PCA(Principal Component Analysis)'))
        dnd.card(ToDo('K - Means Clustering'))
        dnd.card(ToDo('AdaBoost'))
        dnd.card(ToDo('LDA(Linear Discriminant Analysis)'))

    with dnd.column('Deep Learning using Pytorch ', on_drop=handle_drop):
        dnd.card(ToDo('Installation - PyTorch'))
        dnd.card(ToDo('Tensor Basics'))
        dnd.card(ToDo('Autograd'))
        dnd.card(ToDo('Backpropagation'))
        dnd.card(ToDo('Gradient Descent Using Autograd'))
        dnd.card(ToDo('Training Pipeline'))
        dnd.card(ToDo('Linear Regression'))
        dnd.card(ToDo('Logistic Regression'))
        dnd.card(ToDo('Dataset And Dataloader'))
        dnd.card(ToDo('Dataset Transforms'))
        dnd.card(ToDo('Softmax And Cross Entropy'))
        dnd.card(ToDo('Activation Functions'))
        dnd.card(ToDo('Feed Forward Neural Network'))
        dnd.card(ToDo('Convolutional Neural Network(CNN)'))
        dnd.card(ToDo('Transfer Learning'))
        dnd.card(ToDo('Tensorboard'))
        dnd.card(ToDo('Saving And Loading Models'))


ui.run()
