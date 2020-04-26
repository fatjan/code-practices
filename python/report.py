report = [
    {'enrollment': 'rit2011001', 'name': 'Julia', 'subject': [
        {'code': 'NLP', 'grade': 'A'}, {'code': 'DSA', 'grade': 'A'}]},
    {'enrollment': 'rit2011001', 'name': 'Samantha', 'subject': [
        {'code': 'COM', 'grade': 'B'}, {'code': 'OOM', 'grade': 'A'}, {'code': 'DSA', 'grade': 'A'}]}
]
inside = {}
new_report = []
for i in range(len(report)):
    # print(report[i]['subject'])
    for j in range(len(report[i]['subject'])):
        inside['code'] = report[i]['subject'][j]['code']
        inside['grade'] = report[i]['subject'][j]['grade']
        inside['enrollment'] = report[i]['enrollment']
        inside['name'] = report[i]['name']
        new_report.append(inside)
        inside = {}

reports = sorted(new_report, key=lambda report: report['code'])
for i in range(len(reports)):
    for k, v in reports[i].items():
        print(v, end=' ')
    print()

