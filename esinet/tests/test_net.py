import pytest
from .. import simulation
from .. import forward
from .. import Net

# Crate forward model
info = forward.get_info(sfreq=100)
sampling = 'ico3'
fwd = forward.create_forward_model(sampling=sampling)

@pytest.mark.parametrize("duration_of_trial", [0.0, 0.1, (0.0, 0.1)])
@pytest.mark.parametrize("model_type", ['lstm', 'fc', 'convdip'])
def test_net(duration_of_trial,model_type):
    settings = dict(duration_of_trial=duration_of_trial)
    sim = simulation.Simulation(fwd, info, settings=settings)
    sim.simulate(n_samples=2)

    # Create and train net
    net = Net(fwd, n_dense_units=1, n_dense_layers=1, n_lstm_layers=0, model_type=model_type)
    net.fit(sim, batch_size=1, validation_split=0.5, epochs=1)




