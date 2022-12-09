class ExamEvaluator:
    def __init__(self):
        self.no_of_class = int(input('Enter the number of classes held: '))
        self.attended_class = int(input('Enter the number of classes attended: '))
    def attendance_percentage(self):
        percentage = (self.attended_class / self.no_of_class) * 100
        print(f'Percentage of class attended: {percentage}%')
        if percentage < 67:
            print('Not eligible for attend exam')
        else:
            print('Eligible for attend exam')


obj1 = ExamEvaluator()
obj1.attendance_percentage()
