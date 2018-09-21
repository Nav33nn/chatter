class ContractsController < ApplicationController
  def fetch_risk_score
    p params.class
    begin
      result = {message:"",aa:""}
      p "------------------poi1------------"
      response = Contract.new.fetch(params)
      p "-----------poi2--------------"
      p response.inspect

      p "-----------------poi3----------"
    rescue Exception => e
        result[:message] = e.message
        result[:aa] = params
    ensure
      render json: response
    end
  end
end
