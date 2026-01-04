import ROOT

#download from http://opendata.cern.ch/record/12341
input_file = ROOT.TFile("/Users/liamoshaughnessy/Desktop/Summer_Research_2023/CMS/Run2012BC_DoubleMuParked_Muons.root")

#Show what objects are in the file
input_file.ls()

#The proton-proton collision "events" are stored as a ROOT TTree
events_tree = input_file.Get("Events")

print("This tree has {} events".format(events_tree.GetEntries()))

#list all branches (aka variable names) saved in the TTree
events_tree.Print()

#let's print out the info of some of the muons
events_tree.Scan("Muon_pt:Muon_eta:Muon_phi:Muon_charge")

for i,event in enumerate(events_tree):
    print("This event contains {} muons.".format(event.nMuon))
    if event.nMuon>0:
        print("The first muon's pT is {}".format(event.Muon_pt[0]))
    if i>50:
        print("stopping")
        break

input_file.Close()
