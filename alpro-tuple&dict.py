daftar = [   
            {'key': 'MAH001', 'nim': '223200230', 'nama': 'Dwi Prasetia', 'sks': '2', 'beasiswa': '1', 'lahir': '13/12/01'},    
            {'key': 'MAH002', 'nim': '223200231', 'nama': 'Dwi Prasetya', 'sks': '2', 'beasiswa': '0', 'lahir': '14/12/01'},    
            {'key': 'MAH003', 'nim': '223200232', 'nama': 'Dwi Prasetio', 'sks': '2', 'beasiswa': '1', 'lahir': '15/12/01'},    
            {'key': 'MAH004', 'nim': '223200233', 'nama': 'Dwi Prasetyo', 'sks': '2', 'beasiswa': '1', 'lahir': '16/12/01'},    

        ]

print("%-8s"%"Key"+"%-12s"%"NIM"+"%-25s"%"Nama"+"%-5s"%"SKS"+"%-10s"%"Beasiswa"+"%-10s"%"Lahir")
for data in daftar:
    print("%-8s"%data['key']+"%-12s"%data['nim']+"%-25s"%data['nama']+"%-5s"%data['sks']+"%-10s"%data['beasiswa']+"%-10s"%data['lahir'])
