**FAQ**

**What am I looking at?**

You're looking at an atmospheric temperature profile. The air temperature is calculated at three points: at the surface, at a first middle level, and at a second level at the top of the atmosphere.

**Why is it zero all the way up?**

We haven't given the model any information yet. For instance, the starting value for the solar constant, which is how much energy (light) from the sun is reaching Earth, is set at 10 Watts per square meter (W/m^(-2)). With such a low energy input, the Earth would be very cold. Change the value for the solar constant to about 1370 W/m^(-2) – that's about how much it is in real life.

**What are the other values I can change?**

- **Cloud cover** is the percentage of the planet shaded by clouds. The higher the proportion of cloud cover, the more energy from the sun they reflect back to space. Clouds aren't perfect reflectors – even thick white clouds let about a quarter of the sunlight through – but if the whole planet were covered with clouds, it would be quite cold and dark in their shade. The real value for planet Earth is about 35%.
- The **emissitivities** for the upper and lower layers of the atmosphere are values between 0 and 1 that describe how much energy they absorb and emit. Something with a low emissivity won't absorb much energy, so it won't emit much either. The emissitivity of an atmospheric layer is mostly determined by the amount of water it contains; it can be low or high. Try out a few different values.
- The **convective heat fluxes** between layers describe how much energy is transported upwards by non-radiative processes, like the rising of warm air (convection). Like the emissitivity for a given layer, there isn't a single standard constant value in real life. Try some low and high values. What happens if the convective flux from the surface to the first layer is much larger than the convective flux from the first layer to the second layer?

**How do I use the model?**

Adjust the sliders, then click "Calculate model".

**What calculations does the model perform?**

The model solves for the temperature at three points in the atmosphere using a set of matrix equations. For details, see [here](https://biocycle.atmos.colostate.edu/shiny/2layer/).
