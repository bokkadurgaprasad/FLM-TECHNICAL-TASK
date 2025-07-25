import re
#re for pattern matching

def filter_email_subjects(subjects, keyword):
    '''Filters a list of email subjects based on a keyword'''
    filtered_subjects = []
    for subject in subjects:
        if re.search(keyword.lower(), subject.lower()):
            filtered_subjects.append(subject)
    return filtered_subjects

#sample data
sample_subjects = ["New Lead from Form", "Daily Report", "Zoom Invite", "Cybersecurity Lead"]
filtered = filter_email_subjects(sample_subjects, "Lead")
for subject in filtered:
    print(subject)
