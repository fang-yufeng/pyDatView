""" 
Register your plugins in this file:
    1) add a function that calls your plugin. The signature needs to be:
            def _function_name(mainframe, event=None, label='')
       The corpus of this function should import your package
       and call the main function of your package. Your are free
       to use the signature your want for your package

    2) add a tuple to the variable dataPlugins of the form 
         (string, _function_name)

       where string will be displayed under the data menu of pyDatView.

See working examples in this file and this directory.
"""
def _data_mask(label, mainframe):
    from .data_mask import maskAction
    return maskAction(label, mainframe)

# --- plotDataActions
def _data_filter(label, mainframe):
    from .plotdata_filter import filterAction
    return filterAction(label, mainframe)

def _data_sampler(label, mainframe):
    from .plotdata_sampler import samplerAction
    return samplerAction(label, mainframe)

def _data_binning(label, mainframe):
    from .plotdata_binning import binningAction
    return binningAction(label, mainframe)

def _data_removeOutliers(label, mainframe):
    from .plotdata_removeOutliers import removeOutliersAction
    return removeOutliersAction(label, mainframe)

# --- Irreversible actions
def _data_standardizeUnitsSI(label, mainframe=None):
    from .data_standardizeUnits import standardizeUnitsAction
    return standardizeUnitsAction(label, mainframe, flavor='SI')

def _data_standardizeUnitsWE(label, mainframe=None):
    from .data_standardizeUnits import standardizeUnitsAction
    return standardizeUnitsAction(label, mainframe, flavor='WE')


# --- Tools
def _tool_logdec(*args, **kwargs):
    from .tool_logdec import LogDecToolPanel
    return LogDecToolPanel(*args, **kwargs)

def _tool_curvefitting(*args, **kwargs):
    from .tool_curvefitting import CurveFitToolPanel
    return CurveFitToolPanel(*args, **kwargs)

def _tool_radialavg(*args, **kwargs):
    from .tool_radialavg import RadialToolPanel
    return RadialToolPanel(*args, **kwargs)


dataPlugins=[
        # Name/label             , callback                , is a Panel
        ('Mask'                  , _data_mask              , True ),
        ('Remove Outliers'       , _data_removeOutliers    , True ),
        ('Filter'                , _data_filter            , True ),
        ('Resample'              , _data_sampler           , True ),
        ('Bin data'              , _data_binning           , True ),
        ('Standardize Units (SI)', _data_standardizeUnitsSI, False),
        ('Standardize Units (WE)', _data_standardizeUnitsWE, False),
        ]


TOOLS={
 'LogDec':            _tool_logdec,
 'FASTRadialAverage': _tool_radialavg,
 'CurveFitting':      _tool_curvefitting,
}





# ---
def getDataPluginsDict():
    d={}
    for toolName, function, isPanel in dataPlugins:
        d[toolName]={'callback':function, 'isPanel':isPanel}
    return d
