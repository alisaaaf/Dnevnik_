from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from datacenter.models import Mark, Schoolkid, Chastisement, Lesson, Subject, Commendation

def fix_marks(schoolkid):
    Mark.objects.filter(points__in = [2, 3], schoolkid = schoolkid).update(points = 5)

def remove_chastisements(Schoolkid):
    all_comms = Chastisement.objects.filter(schoolkid = Schoolkid)
    all_comms.delete()


def create_commendation(schoolkid, subject_name):
    year_of_study = schoolkid.year_of_study
    letter = schoolkid.group_letter
    subject = Subject.objects.filter(title=subject_name, year_of_study=year_of_study).first()
    lesson = Lesson.objects.filter(year_of_study = year_of_study, group_letter = letter, subject = subject).first()
    teacher = lesson.teacher
    date = lesson.date

    Commendation.objects.create(text='Хвалю!', created = date, schoolkid = schoolkid, subject=subject, teacher= teacher)



if __name__ == '__main__':
    try:
        Ivan = Schoolkid.objects.filter(full_name = 'Фролов Иван Григорьевич').first()
        Feofan = Schoolkid.objects.filter(full_name = 'Голубев Феофан Владленович').first()
        fix_marks(Ivan)
        remove_chastisements(Feofan)
        create_commendation(Ivan, 'Математика')
    except ObjectDoesNotExist:
        print("Ошибка: ученик не найден!")
    except MultipleObjectsReturned:
        print("Ошибка: найдено несколько учеников с таким именем! Уточните запрос.")