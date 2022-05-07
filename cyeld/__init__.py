# =============================================================================
# step23.pyからstep32.pyまではsimple_coreを利用
is_simple_core = False  # True
# =============================================================================

if is_simple_core:
    from cyeld.core_simple import Carray
    from cyeld.core_simple import Function
    from cyeld.core_simple import using_config
    from cyeld.core_simple import no_grad
    from cyeld.core_simple import as_array
    from cyeld.core_simple import as_Carray
    from cyeld.core_simple import setup_Carray

else:
    from cyeld.core import Carray
    from cyeld.core import Parameter
    from cyeld.core import Function
    from cyeld.core import using_config
    from cyeld.core import no_grad
    from cyeld.core import test_mode
    from cyeld.core import as_array
    from cyeld.core import as_Carray
    from cyeld.core import setup_Carray
    from cyeld.core import Config
    from cyeld.layers import Layer
    from cyeld.models import Model
    from cyeld.datasets import Dataset
    from cyeld.dataloaders import DataLoader
    from cyeld.dataloaders import SeqDataLoader

    import cyeld.datasets
    import cyeld.dataloaders
    import cyeld.optimizers
    import cyeld.functions
    import cyeld.functions_conv
    import cyeld.layers
    import cyeld.utils
    import cyeld.cuda
    import cyeld.transforms

setup_Carray()
__version__ = '0.0.1'