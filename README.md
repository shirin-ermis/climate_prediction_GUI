[![Unit tests](https://github.com/shirin-ermis/climate_prediction_GUI/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/shirin-ermis/climate_prediction_GUI/actions/workflows/unit-tests.yml)
[![Run on multiple OS](https://github.com/shirin-ermis/climate_prediction_GUI/actions/workflows/os-test.yml/badge.svg)](https://github.com/shirin-ermis/climate_prediction_GUI/actions/workflows/os-test.yml)
[![codecov](https://codecov.io/gh/shirin-ermis/climate_prediction_GUI/branch/main/graph/badge.svg?token=DLOC4NEPZI)](https://codecov.io/gh/shirin-ermis/climate_prediction_GUI)


# Climate Prediction GUI 🐤

Climate prediction GUI is a package that generates a simple model of vertical energy transfer and temperatures in the Earth system. This model assumes a two-layered atmosphere, to which both layers absorb and reradiate a proportion of the outgoing infrared radiation. The atmosphere is assumed to be transparent to incoming shortwave radiation assuming an albedo $\alpha$. $\alpha$ in turn is determined by the cloudcover, assuming that the planet is either covered by marine stratocumulus $$\alpha_{\mathrm{cloud}}=0.75$$ or open ocean $$\alpha_{\mathrm{ocean}}=0.06$$

The package solves for the temperature of the surface and the two layers in the atmosphere. Users can adjust the values through the GUI, and the temperature profile will be automatically updated to reflect the results from the changed input.

<img src="https://biocycle.atmos.colostate.edu/shiny/2layer/model.png" data-canonical-src="https://biocycle.atmos.colostate.edu/shiny/2layer" width="1112" height="875" />
<sub><sup>Sourced from https://biocycle.atmos.colostate.edu/shiny/2layer/</sup></sub>

## Installation
Install the application by downloading the files below based on your operating system:  
- Mac OS X: `climateprediction.dmg`  
- Windows: `climateprediction.exe`  
- Linux: `climateprediction.deb`

## Usage

## See also

## Authors and acknowledgment
The authors are [Kallista Angeloff][1], [Shirin Ermis][2], [Justin Leung][3], [Adrian Mag][4], [Spencer Pevsner][5] and [Sam Scivier][6]. 

[1]: https://github.com/kallista-angeloff
[2]: https://github.com/shirin-ermis
[3]: https://github.com/justinleung4732
[4]: https://github.com/Adrian-Mag
[5]: https://github.com/synapsidfan
[6]: https://github.com/sscivier
## License
This project uses the [MIT](https://choosealicense.com/licenses/mit/) license. See [LICENSE](https://github.com/shirin-ermis/climate_prediction_GUI/blob/%234readme/LICENSE) for more information. 
