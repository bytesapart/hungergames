import os
import shutil

list_of_pngs = os.listdir("C:\\Users\\iqbal\\Downloads\\captchas_remain")
completed = [tf for tf in list_of_pngs if not tf.startswith('download')]
not_completed = [tfx for tfx in list_of_pngs if tfx.startswith('download')]
print('Total: ' + str(len(completed)) + "/" + str(len(list_of_pngs)))
print('Percentage: ' + str(len(completed) / len(list_of_pngs) * 100))

dupes = [d for d in completed if '(' in d]
print('Dupes: ' + str(len(dupes)))
print('Total Dupes: ' + str(len(dupes)) + "/" + str(len(completed)))
print('Percentage Dupes: ' + str(len(dupes) / len(completed) * 100))

# dest = "C:\\Users\\iqbal\\Downloads\\captchas_2k"
# dest2 = "C:\\Users\\iqbal\\Downloads\\captchas_remain"
# full_not_completed = [os.path.join("C:\\Users\\iqbal\\Downloads\\captchaspng", fnc) for fnc in not_completed]
# full_not_completed_main = full_not_completed[:2000]
# full_not_completed_peripheral = full_not_completed[2000:]
#
# for item in full_not_completed_main:
#     shutil.copy(item, os.path.join(dest, os.path.basename(item)))
#
# for item in full_not_completed_peripheral:
#     shutil.copy(item, os.path.join(dest2, os.path.basename(item)))

