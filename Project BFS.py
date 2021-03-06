#start = ALASKA
#finish = GEORGIA
#path

maps =  {'ALASKA':set(['CALIFORNIA']),
         'CALIFORNIA':set(['CAROLINA','ALASKA']),
         'CAROLINA':set(['CALIFORNIA','INDIANA','HAWAII','DAREWALE']),
         'DAREWALE':set(['CAROLINA','EDINBURH','HAWAII','FLORIDA']),
         'EDINBURGH':set(['DAREWALE']),
         'FLORIDA':set(['DAREWALE','GEORGIA']),
         'GEORGIA':set(['FLORIDA','HAWAII']),
         'HAWAII':set(['DARAWALE','CAROLINA','GEORGIA','LOUSIANA']),
         'INDIANA':set(['CAROLINA','IDAKO','KENTUCKY']),
         'IDAKO':set(['INDIANA']),
         'KENTUCKY':set(['LOUSIANA','INDIANA']),
         'LOUSIANA':set(['KENTUCKY','HAWAII'])}

def bfs(graf, start, finish):
    queue = [[start]]
    visited = set()

    while queue:     
        # masukkan antrian paling depan ke variabel jalur
        path = queue.pop(0)

        # simpan node yang dipilih ke variabel state, misal jalur = C,B maka simpan B ke variabel state
        state = path[-1]

        # cek state apakah sama dengan tujuan, jika ya maka return jalur
        if state == finish:
            return path
        # jika state tidak sama dengan tujuan, maka cek apakah state tidak ada di visited
        elif state not in visited:
            # jika state tidak ada di visited maka cek cabang
            for branch in graf.get(state, []): #cek semua cabang dari state
                new_path = list(path) #masukkan isi dari variabel jalur ke variabel jalur_baru
                new_path.append(branch) #update/tambah isi jalur_baru dengan cabang
                queue.append(new_path) #update/tambah queue dengan jalur_baru

            # tandai state yang sudah dikunjungi sebagai visited
            visited.add(state)

        #cek isi antrian
        content = len(queue)
        if content == 0:
            print("NOT FOUND 404")

print(bfs(maps,'ALASKA','GEORGIA'))
