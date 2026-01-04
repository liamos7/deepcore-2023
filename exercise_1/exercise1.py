import ROOT
from ROOT import Math

#%%

## Plot 1D histograms of the pT, eta, and phi of all muons
input_file = ROOT.TFile("/Users/liamoshaughnessy/Desktop/Summer_Research_2023/CMS/Run2012BC_DoubleMuParked_Muons.root")
events_tree = input_file.Get("Events")

h1 = ROOT.TH1F("h1", "pT;pT_Value;Frequency", 100, -20, 70)
h2 = ROOT.TH1F("h2", "eta;eta_Value;Frequency", 100, -10, 10)
h3 = ROOT.TH1F("h3", "phi;phi_Value;Frequency", 100, -10, 10)

for j,event in enumerate(events_tree):
    for i in range(event.nMuon):
        h1.Fill(event.Muon_pt[i])
        h2.Fill(event.Muon_eta[i])
        h3.Fill(event.Muon_phi[i])
    if j == 2000000:
        break
h1.Draw()
h2.Draw()
h3.Draw()
canvas = ROOT.TCanvas("canvas", "Canvas Title", 800, 600)
canvas.Divide(2, 2)  # Divide the canvas into a 2x2 grid

canvas.cd(1)
h1.Draw()

canvas.cd(2)
h2.Draw()

canvas.cd(3)
h3.Draw()

canvas.cd(4)
combinedPad = ROOT.TPad("combinedPad", "Combined Pad", 0, 0, 1, 1)
combinedPad.Divide(2, 2)
combinedPad.cd(1)
h1.Draw()

combinedPad.cd(2)
h2.Draw()

combinedPad.cd(3)
h3.Draw()

combinedPad.SaveAs("1-D_Histograms.jpg")

input_file.Close()

#%% 
# Plot a 2D histogram of muon's eta vs phi
input_file = ROOT.TFile("/Users/liamoshaughnessy/Desktop/Summer_Research_2023/CMS/Run2012BC_DoubleMuParked_Muons.root")
events_tree = input_file.Get("Events")

histogram = ROOT.TH2F("histogram", "Muon Data;eta;phi", 100, -7, 7, 100, -5, 5)
for j,event in enumerate(events_tree):
    for i in range(event.nMuon):
        histogram.Fill(event.Muon_eta[i], event.Muon_phi[i])
    if j == 2000000:
        break
canvas = ROOT.TCanvas("canvas", "2-D Plot", 800, 600)
histogram.Draw("COLZ")  # "COLZ" option displays color-coded cells
canvas.Update()
canvas.SaveAs("Eta_v_Phi.jpg")
input_file.Close()

#%%
## For events containing two oppositely-charged muons, calculate the angular separation (deltaR) of the two muons and plot it
input_file = ROOT.TFile("/Users/liamoshaughnessy/Desktop/Summer_Research_2023/CMS/Run2012BC_DoubleMuParked_Muons.root")
events_tree = input_file.Get("Events")

canvas = ROOT.TCanvas("canvas", "Angular Separation", 800, 600)
histogram = ROOT.TH1F("h1", "Angular Separation;Delta_R;Frequency", 100, 0, 7)

for j,event in enumerate(events_tree):
    if (event.nMuon == 2):
        if event.Muon_charge[0] != event.Muon_charge[1]:
            histogram.Fill(ROOT.TMath.Sqrt(ROOT.TMath.Power(event.Muon_eta[1]-event.Muon_eta[0],2) + ROOT.TMath.Power(event.Muon_phi[1]-event.Muon_phi[0],2)))
    if j == 2000000:
        break
histogram.Draw()
canvas.Update()
canvas.SaveAs("Angular_Separation.jpg")
input_file.Close()

#%%
## For events containing two oppositely-charged muons, compute the invariant mass of the muon pair by constructing each muon's 4-vector with ROOT.TLorentzVector and summing the two 4-vectors. Then plot the mass and see if there's a peak around 90 GeV for the Z boson

input_file = ROOT.TFile("/Users/liamoshaughnessy/Desktop/Summer_Research_2023/CMS/Run2012BC_DoubleMuParked_Muons.root")
events_tree = input_file.Get("Events")

canvas = ROOT.TCanvas("canvas", "Mass", 800, 600)
histogram = ROOT.TH1F("h1", "Invariant Mass;Mass;Frequency", 100, 0, 120)

for j,event in enumerate(events_tree):
    if (event.nMuon == 2):
        if event.Muon_charge[0] != event.Muon_charge[1]:
            v1 = ROOT.Math.PtEtaPhiMVector(event.Muon_pt[0], event.Muon_eta[0],event.Muon_phi[0],event.Muon_mass[0])
            v2 = ROOT.Math.PtEtaPhiMVector(event.Muon_pt[1], event.Muon_eta[1],event.Muon_phi[1],event.Muon_mass[1])
            histogram.Fill((v1+v2).M())
    if j == 2000000:
        break
histogram.Draw()
canvas.Update()
canvas.SaveAs("Invariant_Mass.jpg")
input_file.Close()   