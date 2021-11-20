import os
from pathlib import Path

styles = [
    [
        'data/classical/beethoven',
        'data/classical/haydn',
        'data/classical/mozart'
    ],
    [
        'data/romantic/borodin',
        'data/romantic/brahms',
        'data/romantic/tschai'
    ]
]

dataurls = [
    [
        [
            'http://www.piano-midi.de/midis/beethoven/beethoven_opus10_1_format0.mid',
            'http://www.piano-midi.de/midis/beethoven/beethoven_opus10_2_format0.mid',
            'http://www.piano-midi.de/midis/beethoven/beethoven_opus10_3_format0.mid',
            'http://www.piano-midi.de/midis/beethoven/pathetique_1_format0.mid',
            'http://www.piano-midi.de/midis/beethoven/pathetique_2_format0.mid',
            'http://www.piano-midi.de/midis/beethoven/pathetique_3_format0.mid',
            'http://www.piano-midi.de/midis/beethoven/beethoven_opus22_1_format0.mid',
            'http://www.piano-midi.de/midis/beethoven/beethoven_opus22_2_format0.mid',
            'http://www.piano-midi.de/midis/beethoven/beethoven_opus22_3_format0.mid',
            'http://www.piano-midi.de/midis/beethoven/beethoven_hammerklavier_1_format0.mid',
            'http://www.piano-midi.de/midis/beethoven/beethoven_hammerklavier_2_format0.mid',
            'http://www.piano-midi.de/midis/beethoven/beethoven_hammerklavier_3_format0.mid'
        ],
        [
            'http://www.piano-midi.de/midis/haydn/haydn_7_1_format0.mid',
            'http://www.piano-midi.de/midis/haydn/haydn_7_2_format0.mid',
            'http://www.piano-midi.de/midis/haydn/haydn_7_3_format0.mid',
            'http://www.piano-midi.de/midis/haydn/haydn_8_1_format0.mid',
            'http://www.piano-midi.de/midis/haydn/haydn_8_2_format0.mid',
            'http://www.piano-midi.de/midis/haydn/haydn_8_3_format0.mid',
            'http://www.piano-midi.de/midis/haydn/haydn_8_4_format0.mid',
            'http://www.piano-midi.de/midis/haydn/haydn_9_1_format0.mid',
            'http://www.piano-midi.de/midis/haydn/haydn_9_2_format0.mid',
            'http://www.piano-midi.de/midis/haydn/haydn_9_3_format0.mid',
            'http://www.piano-midi.de/midis/haydn/haydn_43_1_format0.mid',
            'http://www.piano-midi.de/midis/haydn/haydn_43_2_format0.mid',
            'http://www.piano-midi.de/midis/haydn/haydn_43_3_format0.mid'
        ],
        [
            'http://www.piano-midi.de/midis/mozart/mz_311_1_format0.mid',
            'http://www.piano-midi.de/midis/mozart/mz_311_2_format0.mid',
            'http://www.piano-midi.de/midis/mozart/mz_311_3_format0.mid',
            'http://www.piano-midi.de/midis/mozart/mz_330_1_format0.mid',
            'http://www.piano-midi.de/midis/mozart/mz_330_2_format0.mid',
            'http://www.piano-midi.de/midis/mozart/mz_330_3_format0.mid',
            'http://www.piano-midi.de/midis/mozart/mz_331_1_format0.mid',
            'http://www.piano-midi.de/midis/mozart/mz_331_2_format0.mid',
            'http://www.piano-midi.de/midis/mozart/mz_331_3_format0.mid',
            'http://www.piano-midi.de/midis/mozart/mz_570_1_format0.mid',
            'http://www.piano-midi.de/midis/mozart/mz_570_2_format0.mid',
            'http://www.piano-midi.de/midis/mozart/mz_570_3_format0.mid'
        ]
        
    ],
    [
        [
            'http://www.piano-midi.de/midis/borodin/bor_ps1_format0.mid',
            'http://www.piano-midi.de/midis/borodin/bor_ps2_format0.mid',
            'http://www.piano-midi.de/midis/borodin/bor_ps3_format0.mid',
            'http://www.piano-midi.de/midis/borodin/bor_ps1_format4.mid',
            'http://www.piano-midi.de/midis/borodin/bor_ps1_format5.mid',
            'http://www.piano-midi.de/midis/borodin/bor_ps6_format0.mid',
            'http://www.piano-midi.de/midis/borodin/bor_ps7_format0.mid'
        ],
        [
            'http://www.piano-midi.de/midis/brahms/brahms_opus1_1_format0.mid',
            'http://www.piano-midi.de/midis/brahms/brahms_opus1_2_format0.mid',
            'http://www.piano-midi.de/midis/brahms/brahms_opus1_3_format0.mid',
            'http://www.piano-midi.de/midis/brahms/brahms_opus1_4_format0.mid',
            'http://www.piano-midi.de/midis/brahms/br_im2_format0.mid',
            'http://www.piano-midi.de/midis/brahms/br_im5_format0.mid',
            'http://www.piano-midi.de/midis/brahms/br_im6_format0.mid',
            'http://www.piano-midi.de/midis/brahms/brahms_opus117_1_format0.mid',
            'http://www.piano-midi.de/midis/brahms/brahms_opus117_2_format0.mid',
            'http://www.piano-midi.de/midis/brahms/br_rhap_format0.mid'
        ],
        [
            'http://www.piano-midi.de/midis/tchaikovsky/ty_januar_format0.mid',
            'http://www.piano-midi.de/midis/tchaikovsky/ty_februar_format0.mid',
            'http://www.piano-midi.de/midis/tchaikovsky/ty_maerz_format0.mid',
            'http://www.piano-midi.de/midis/tchaikovsky/ty_april_format0.mid',
            'http://www.piano-midi.de/midis/tchaikovsky/ty_mai_format0.mid',
            'http://www.piano-midi.de/midis/tchaikovsky/ty_juni_format0.mid',
            'http://www.piano-midi.de/midis/tchaikovsky/ty_juli_format0.mid',
            'http://www.piano-midi.de/midis/tchaikovsky/ty_august_format0.mid',
            'http://www.piano-midi.de/midis/tchaikovsky/ty_september_format0.mid',
            'http://www.piano-midi.de/midis/tchaikovsky/ty_oktober_format0.mid',
            'http://www.piano-midi.de/midis/tchaikovsky/ty_november_format0.mid',
            'http://www.piano-midi.de/midis/tchaikovsky/ty_dezember_format0.mid'
        ]
    ]
]

def downloadDataset(styles, dataurls):
    for i, style in enumerate(styles):
        for j, dir in enumerate(style):
            Path(dir).mkdir(parents=True, exist_ok=True)
            for item in dataurls[i][j]:
                os.system('wget -q {} -P {}'.format(item, dir))

if __name__ == '__main__':
    downloadDataset(styles, dataurls)