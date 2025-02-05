import matplotlib.pyplot
import de_embedding_algorithms
import numpy
import skrf
import matplotlib

y = de_embedding_algorithms.TRL().thru2x(r'.\de_embedding\cal_std\sim\thru.s2p', export_path=r'.\de_embedding\cal_std\sim') 
y = de_embedding_algorithms.TRL().thru2x(r'.\de_embedding\cal_std\meas\thru.s2p', export_path=r'.\de_embedding\cal_std\meas') 
y = de_embedding_algorithms.TRL().thru2x(r'.\de_embedding\cal_std\comp_sim\fixture_thru_fixture.s2p', export_path=r'.\de_embedding\cal_std\comp_sim') 
