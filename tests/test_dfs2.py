import os
import numpy as np
import datetime

from pydhi import dfs2 as dfs2


def test_simple_create():

    filename = r"simple.dfs2"

    data = []

    nt = 100
    nx = 20
    ny = 5
    d = np.random.random([nt, ny, nx])

    data.append(d)

    dfs = dfs2.dfs2()

    dfs.create(filename=filename, data=data)

    assert True
    os.remove(filename)


def test_create_single_item():

    start_time = datetime.datetime(2012, 1, 1)

    # timeseries_unit = second=1400, minute=1401, hour=1402, day=1403, month=1405, year= 1404
    timeseries_unit = 1402
    dt = 12

    variable_type = [100000]
    unit = [1000]

    filename = r"random.dfs2"

    data = []
    d = np.random.random([100, 2, 3])
    d[10, :, :] = np.nan
    d[11, :, :] = 0
    d[12, :, :] = 1e-10
    d[13, :, :] = 1e10

    data.append(d)
    # >>> from pyproj import Proj
    # >>> utm = Proj(32633)
    # >>> utm(12.0, 55.0)
    east = 308124
    north = 6098907
    orientation = 0

    coordinate = ['UTM-33', east, north, orientation]
    length_x = 100
    length_y = 100

    names = ['testing water level']
    title = 'test dfs2'

    dfs = dfs2.dfs2()

    dfs.create(filename=filename, data=data,
               start_time=start_time,
              timeseries_unit=timeseries_unit,
              dt=dt, variable_type=variable_type,
              unit=unit,
              coordinate=coordinate,
              length_x=length_x,
              length_y=length_y,
              names=names, title=title)

    assert True
    os.remove(filename)


def test_create_multiple_item():

    start_time = datetime.datetime(2012, 1, 1)

    # timeseries_unit = second=1400, minute=1401, hour=1402, day=1403, month=1405, year= 1404
    timeseries_unit = 1402
    dt = 12

    # from result we see Water Level is 100000, Rainfall is 100004, drain time constant 100362
    variable_type = [100000, 100004, 100362]

    #possible_units = util.unit_list(variable_type, search='meter')
    # from result, we see meter is 1000 and milimeter is 1002, per second is 2605
    unit = [1000, 1002, 2605]

    filename = r"multiple.dfs2"

    data = []
    d = np.zeros([100, 100, 30]) + 1.0
    data.append(d)
    d = np.zeros([100, 100, 30]) + 2.0
    data.append(d)
    d = np.zeros([100, 100, 30]) + 3.0
    data.append(d)

    coordinate = ['LONG/LAT', 12.4387, 55.2257, 0]
    length_x = 0.1
    length_y = 0.1

    names = ['testing water level', 'testing rainfall', 'testing drain time constant']
    title = 'test dfs2'

    dfs = dfs2.dfs2()

    dfs.create(filename=filename, data=data,
               start_time=start_time,
               timeseries_unit=timeseries_unit, dt=dt,
               variable_type=variable_type,
               unit=unit, coordinate=coordinate,
               length_x=length_x, length_y=length_y,
               names=names, title=title)

    assert True
    os.remove(filename)


def test_non_equidistant_calendar():

    filename = r"neq.dfs2"

    data = []

    datetimes = [datetime.datetime(2012, 1, 1),
                 datetime.datetime(2012, 2, 1)]

    nt = len(datetimes)
    nx = 20
    ny = 5
    d = np.random.random([nt, ny, nx])

    data.append(d)

    dfs = dfs2.dfs2()

    dfs.create(filename=filename, data=data, datetimes=datetimes)

    assert True
    os.remove(filename)



def test_read():

    filename = r"tests/testdata/random.dfs2"
    dfs = dfs2.dfs2()

    data = dfs.read(filename, [0])[0]
    data = data[0]
    assert data[0, 11, 0] == 0
    assert np.isnan(data[0, 10, 0])
    assert data.shape == (3, 100, 2) # time, y, x


def test_write():

    pass



