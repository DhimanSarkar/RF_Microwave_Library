import matplotlib.pyplot
import de_embedding_algorithms
import numpy
import skrf
import matplotlib

# y = de_embedding_algorithms.TRL().thru2x(r'.\de_embedding\cal_std\sim\thru.s2p', export_path=r'.\de_embedding\cal_std\sim') 
# y = de_embedding_algorithms.TRL().thru2x(r'.\de_embedding\cal_std\meas\thru.s2p', export_path=r'.\de_embedding\cal_std\meas') 
# y = de_embedding_algorithms.TRL().thru2x(r'.\de_embedding\cal_std\comp_sim\fixture_thru_fixture.s2p', export_path=r'.\de_embedding\cal_std\comp_sim') 

# y = de_embedding_algorithms.TRL().thru2x(r'.\de_embedding\cal_std\meas\v2\1\THRU1.s2p', export_path=r'.\de_embedding\cal_std\meas\v2\1') 
# y = de_embedding_algorithms.TRL().thru2x(r'.\de_embedding\cal_std\meas\v2\2\THRU2.s2p', export_path=r'.\de_embedding\cal_std\meas\v2\2') 

y = de_embedding_algorithms.TRL().TRL(r'.\de_embedding\cal_std\meas\focus\thru.s2p',r'.\de_embedding\cal_std\meas\focus\refl.s2p',r'.\de_embedding\cal_std\meas\focus\line.s2p', export_path=r'.\de_embedding\cal_std\meas\focus') 