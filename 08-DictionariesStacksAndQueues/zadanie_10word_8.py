a=[{
    'kraj': 'Polska',
    "populacja": 38000000
},
{
    'kraj': 'Czechy',
    "populacja": 38746000
},
{
    'kraj': 'Austria',
    "populacja": 38354300
},
{
    'kraj': 'Norwegia',
    "populacja": 38076570
},
{
    'kraj': 'Hiszpania',
    "populacja": 24545600
    }]


x=0
while x<len(a):
    # print(a[x])
    for key,value in a[x].items():
        print(key,':',value)
    x=x+1