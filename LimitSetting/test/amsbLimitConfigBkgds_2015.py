#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '0',
        'alpha' : '0.0694017067366',
    },
    'Elec' : {
        'N' : '2',
        'alpha' : '0.0850204059032',
    },
    'Muon' : {
        'N' : '0',
        'alpha' : '0.0476425834662',
    },
    'Tau' : {
        'N' : '3',
        'alpha' : '0.004255546101',
    },
}

background_systematics = {
    'Fake_alpha' : { # error on alpha
        'value' : '1.17035368779',
        'background'  : 'Fake',
    },
    'Elec_alpha' : { # error on alpha
        'value' : '1.02313291551',
        'background'  : 'Elec',
    },
    'Muon_alpha' : { # error on alpha
        'value' : '1.01102047869',
        'background'  : 'Muon',
    },
    'Tau_alpha' : { # error on alpha
        'value' : '1.9688036674',
        'background'  : 'Tau',
    },



    'Fake_syst' : { # error on fake track rate assumption
        'value' : str (1.0 + 100.0 / 100.0),
        'background'  : 'Fake',
    },
    'Elec_energy' : { # error on energy assumption
        'value' : str (1.0 + 10.2310902711 / 100.0),
        'background'  : 'Elec',
    },
    'Tau_energy' : { # error on energy assumption
        'value' : str (1.0 + 20.0749726096 / 100.0),
        'background'  : 'Tau',
    },
}
