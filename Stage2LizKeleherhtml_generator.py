TEXT= """TITLE: Work Session 1 Notes
CONCEPT: Search Engines
TITLE: Work Session 2 Notes
CONCEPT: Variables
TITLE: Work Session 3 Notes
CONCEPT: Functions"""


def generate_work_session_HTML(work_session_title, concept):
	html_text_1= '''
<div class="work-session">
<h2>''' + work_session_title
	html_text_2= '''</h2>
	<div class="concept">
	<h3>''' + concept
	html_text_3= '''</h3>
		<div class="supporting-info">
		</div>
	</div>'''
	full_html_text= html_text_1 + html_text_2 + html_text_3
	return full_html_text

##After running generate_all_html(TEXT) I would go back and add in the rest of the notes for each work session.  This process has really helped me understand how functions can help me avoid repetition and allow me to make changes to my code more easily.

def get_work_session_title(workSession):
	start_location = workSession.find('TITLE:')
	end_location = workSession.find('CONCEPT:')
	work_session_title = workSession[start_location+7 : end_location-1]
	return work_session_title

##this works and I get: Work Session 1 Notes

def get_concept(concept):
	start_location = concept.find('CONCEPT:')
	concept = concept[start_location+9 :-1]
	return concept

#this works and I get: Search Engines

def get_work_session_by_number(text, work_session_number):
	counter= 0 
	while counter < work_session_number:
		counter = counter + 1
		next_work_session_start= text.find('TITLE:')
		next_work_session_end= text.find('TITLE:', next_work_session_start + 1)
		if next_work_session_end >= 0:
			work_session = text[next_work_session_start:next_work_session_end]
		else:
			next_work_session_end = len(text)
			work_session = text[next_work_session_start:]
		text = text[next_work_session_end:]
	return work_session

#print get_work_session_by_number(TEXT, 3) test worked

def generate_all_html(text):
	current_work_session_number = 1
	work_session = get_work_session_by_number(text, current_work_session_number)
	all_html= ''
	while work_session != '':
		work_session_title = get_work_session_title(work_session)
		concept = get_concept(work_session)
		work_session_html = generate_work_session_HTML(work_session_title, concept)
		all_html = all_html + work_session_html
		current_work_session_number = current_work_session_number + 1
		work_session = get_work_session_by_number(text, current_work_session_number)
	return all_html

print generate_all_html(TEXT)