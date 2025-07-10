from flask import Flask, render_template, request
app= Flask(__name__)



Jobs=[
    {
        id:1,
        'title':'Software Engineer',
        'description':'Develop and maintain software applications.',
        'location':'San Francisco, CA',
        'salary':'$120,000 - $150,000',
        'skills':['Python', 'JavaScript', 'SQL'],
        'company':'Tech Innovations Inc.',
        'date_posted':'2023-10-01',
    },

    {
        id:2,
        'title':'Data Scientist',
        'description':'Analyze and interpret complex data sets.',
        'location':'New York, NY',
        'salary':'$110,000 - $140,000',
        'skills':['Python', 'R', 'Machine Learning'],
        'company':'Data Insights LLC',
        'date_posted':'2023-09-25',
    },

    {
        id:3,
        'title':'Web Developer',
        'description':'Build and maintain websites and web applications.',
        'location':'Remote',
        'salary':'$80,000 - $100,000',
        'skills':['HTML', 'CSS', 'JavaScript'],
        'company':'Web Solutions Co.',
        'date_posted':'2023-10-05',
    },
    {
        id:4,
        'title':'Project Manager',
        'description':'Oversee projects from inception to completion.',
        'location':'Chicago, IL',
        'salary':'$90,000 - $120,000',
        'skills':['Project Management', 'Agile', 'Communication'],
        'company':'Global Projects Ltd.',
        'date_posted':'2023-09-30',
    },

    {
        id:5,
        'title':'UX/UI Designer',
        'description':'Design user-friendly interfaces and experiences.',
        'location':'Austin, TX',
        'salary':'$70,000 - $90,000',
        'skills':['Figma', 'Adobe XD', 'User Research'],
        'company':'Creative Designs Inc.',
        'date_posted':'2023-10-03',
    }
]


@app.route('/')
def homepage():
    return render_template('index.html',jobs=Jobs)



@app.route('/findJobs')
def findJobs():
    return render_template('findJobs.html')


@app.route('/find_jobs', methods=['POST'])
def find_jobs():
    job_title = request.form['jobTitle'].lower()
    location = request.form['location'].lower()

    filtered_jobs = [
        job for job in Jobs
        if job_title in job['title'].lower() and location in job['location'].lower()
    ]
    return render_template('jobs.html', jobs=filtered_jobs)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')