import json
import os



def get_fiels_name(path):
    list_files = []
    for root, dirs,file_names in os.walk(path):
        for file in file_names:
            if os.path.splitext(file)[1] == ".json":
                    list_files.append(os.path.splitext(file)[0])
    return list_files
list_train = get_fiels_name("Kinetics\kinetics-skeleton\kinetics_train")
list_val = get_fiels_name("Kinetics\kinetics-skeleton\kinetics_val")


def json_new(path_old,path_new,file_list):
    with open(path_old) as json_file:
        train_json = json.load(json_file)
        # print(train_json)
    tmp_dict = dict()
    for train_file in file_list:
        print(train_json[train_file])
        tmp_dict[train_file] = train_json[train_file]
    with open(path_new,"w") as json_dumps:
        json.dump(tmp_dict,json_dumps)

json_new("Kinetics/kinetics-skeleton/kinetics_train_label.json","Kinetics/kinetics-skeleton/new_kinetics_train_label.json",list_train)
json_new("Kinetics/kinetics-skeleton/kinetics_val_label.json","Kinetics/kinetics-skeleton/new_kinetics_val_label.json",list_val)